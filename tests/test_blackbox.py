from calculator import safe_eval

# ECP

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
    assert safe_eval("3*/2") == "Unsupported expression"


def test_ecp_division_by_zero():
    assert safe_eval("9/0") == "Error: Cannot Divide by zero"

# BVA

def test_bva_min_digit():
    assert safe_eval("1") == 1


def test_bva_just_below_limit():
    assert safe_eval("99999999") == 99999999

def test_bva_max_valid_digits():
    assert safe_eval("999999999") == 999999999


def test_bva_exceeds_limit():
    assert safe_eval("1000000000") == "Error: Number too large (max 9 digits)"



def test_bva_expression_with_max_digits():
    assert safe_eval("999999999+1") == 1000000000


def test_bva_expression_exceeding_digits():
    assert safe_eval("1000000000+1") == "Error: Number too large (max 9 digits)"


def test_bva_decimal_within_limit():
    assert safe_eval("12345.6789") == 12345.6789


def test_bva_decimal_exceeds_limit():
    assert safe_eval("123456789.1") == "Error: Number too large (max 9 digits)"