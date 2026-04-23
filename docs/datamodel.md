# Calculator Application Data Model

## Overview

This application is a web-based calculator built using FastAPI (backend) and HTML/JavaScript (frontend). It is stateless and does not use a database. The data model focuses on request/response interactions and internal expression evaluation.

---

## System Components

- **Frontend (Calculator UI)**: Handles user input and display
- **Backend (FastAPI Service)**: Processes expressions and returns results

---

## Entities

### 1. Calculator UI

Represents the browser-based interface.

**Attributes:**
- `display` (string): Current expression or result shown to the user
- `buttons` (collection): Input controls (digits, operators, actions)

**Relationships:**
- Sends expressions to backend
- Receives results from backend

---

### 2. Expression Request

Represents the data sent from frontend to backend.

**Schema:**
```json
{
  "expression": "string"
}
```

**Attributes:**
- `expression` (string): Arithmetic expression (e.g., "3+4*2")

---

### 3. Calculation Result

Represents the backend response.

**Schema:**
```json
{
  "result": "number | string"
}
```

**Attributes:**
- `result` (int | float | string): Computed result or error message

---

### 4. Expression

Logical representation of the input expression.

**Attributes:**
- `raw_expression` (string)
- `tokens` (implicit): numbers, operators, parentheses
- `evaluated_value` (number or error)

---

### 5. AST Node (Internal)

Represents parsed expression structure.

**Attributes:**
- `node_type` (Constant, UnaryOp, BinOp)
- `operator` (+, -, *, /)
- `left` (node)
- `right` (node)
- `operand` (node)

---

## Relationships

```text
User Input
   ↓
Calculator UI
   ↓
Expression Request (JSON)
   ↓
Backend Parser (AST)
   ↓
Evaluation
   ↓
Calculation Result (JSON)
   ↓
UI Display
```

---

## Data Types

- `string` → expressions, display, errors
- `integer` → whole number results
- `float` → decimal results
- `JSON` → API communication

---

## Constraints

- Only basic arithmetic supported (+, -, *, /)
- Supports negative numbers and parentheses
- Invalid expressions return "Error"
- Division by zero handled explicitly
- No persistent storage

---

## Summary

The calculator uses a simple, stateless data model centered on processing arithmetic expressions. Communication is handled via JSON between the frontend and backend, and expressions are evaluated safely using Python's AST parsing.

