from calculator import safe_eval

# ECP: Equivalence Class Partitioning

def test_ecp_valid_integer_expression():
    assert safe_eval("6+2") == 8

def test_ecp_valid_decimal_expression():
    assert safe_eval("7/2") == 3.5

def test_ecp_valid_negative_expression():
    assert safe_eval("-5+3") == -2

def test_ecp_valid_parentheses_expression():
    assert safe_eval("(3+5)*2") == 16

def test_ecp_invalid_characters():
    assert safe_eval("2+a") == "Error"

def test_ecp_invalid_syntax():
    assert safe_eval("3*/2") == "Error"

def test_ecp_division_by_zero():
    assert safe_eval("9/0") == "Error: Divide by zero"