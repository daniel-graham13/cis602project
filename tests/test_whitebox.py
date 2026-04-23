from calculator import safe_eval, normalize_expression

# Statement coverage:


def test_statement_valid_addition():
    assert safe_eval("2+3") == 5


def test_statement_divide_by_zero():
    assert safe_eval("5/0") == "Error: Divide by zero"


def test_statement_invalid_expression():
    assert safe_eval("2++") == "Error"



# Block coverage:


def test_block_constant_and_binop():
    assert safe_eval("8-3") == 5


def test_block_unary_negative():
    assert safe_eval("-4+1") == -3


def test_block_parentheses():
    assert safe_eval("(2+3)*4") == 20



# Condition coverage:


def test_condition_float_is_integer_true():
    assert safe_eval("8/4") == 2   # result is 2.0 -> converted to int 2


def test_condition_float_is_integer_false():
    assert safe_eval("7/2") == 3.5


def test_condition_normalize_number_before_paren():
    assert normalize_expression("8(9)") == "8*(9)"


def test_condition_normalize_close_paren_before_number():
    assert normalize_expression("(2+3)4") == "(2+3)*4"


def test_condition_normalize_close_paren_before_open_paren():
    assert normalize_expression("(2+3)(4+1)") == "(2+3)*(4+1)"


def test_condition_normalize_number_before_paren():
    assert normalize_expression("8(9)") == "8*(9)"


def test_condition_normalize_close_paren_before_number():
    assert normalize_expression("(2+3)4") == "(2+3)*4"


def test_condition_normalize_close_paren_before_open_paren():
    assert normalize_expression("(2+3)(4+1)") == "(2+3)*(4+1)"



# Path coverage:


def test_path_normal_expression():
    assert safe_eval("3*4+2") == 14


def test_path_unary_then_binop():
    assert safe_eval("-2*5") == -10


def test_path_implicit_multiplication_then_eval():
    assert safe_eval("8(9)/7+3") == 93/7


def test_path_invalid_syntax():
    assert safe_eval("((3") == "Error"


def test_path_zero_division_after_parsing():
    assert safe_eval("(4+1)/(3-3)") == "Error: Divide by zero"
