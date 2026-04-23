from pathlib import Path
import ast
import operator as op   

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

import re

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent
HTML_PATH = BASE_DIR / "index.html"

# Allowed operators for safe evaluation
ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.USub: op.neg,
}


class ExpressionRequest(BaseModel):
    expression: str

def normalize_expression(expr: str) -> str:             

    expr = re.sub(r'(\d)\(', r'\1*(', expr)

    expr = re.sub(r'\)(\d)', r')*\1', expr)

    expr = re.sub(r'\)\(', r')*(', expr)

    return expr

MAX_DIGITS = 9

def validate_expression(expr: str):
    numbers = re.findall(r'\d+\.?\d*', expr)

    for num in numbers:
        digit_count = len(num.replace('.', ''))

        if digit_count > MAX_DIGITS:
            raise ValueError("Error: Number too large (max 9 digits)")


def safe_eval(expression: str):                         
    """Safely evaluate a simple arithmetic expression."""
    try:
        expression = normalize_expression(expression)
        validate_expression(expression)

        node = ast.parse(expression, mode="eval").body
        result = evaluate_node(node)
        
        if isinstance(result, float) and result.is_integer():
            return int(result)
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except Exception:
        return "Error"


def evaluate_node(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.UnaryOp) and type(node.op) in ALLOWED_OPERATORS:
        operand = evaluate_node(node.operand)
        return ALLOWED_OPERATORS[type(node.op)](operand)

    if isinstance(node, ast.BinOp) and type(node.op) in ALLOWED_OPERATORS:
        left = evaluate_node(node.left)
        right = evaluate_node(node.right)
        return ALLOWED_OPERATORS[type(node.op)](left, right)

    raise ValueError("Unsupported expression")


@app.get("/", response_class=HTMLResponse)
async def home():
    return HTML_PATH.read_text(encoding="utf-8")


@app.post("/calculate")
async def calculate_expression(request: ExpressionRequest):
    return {"result": safe_eval(request.expression)}