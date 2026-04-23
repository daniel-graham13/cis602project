# Testing
<br>


## Overview



This page documents the calculator application's white-box and black-box test cases.

The calculator enforces a **maximum of 9 digits per numeric input**. Any number with more than 9 digits returns an error.

---

## White-Box Testing
<br>


### Statement Coverage Criteria

| Test ID | Input | Expected Output | Purpose |
|---|---|---|---|
| SC-1 | `2+3` | `5` | Covers normal evaluation statements |
| SC-2 | `5/0` | `Error: Divide by zero` | Covers divide-by-zero exception path |
| SC-3 | `2++` | `Error` | Covers invalid-expression error handling |
| SC-4 | `1000000000` | `Error: Number too large (max 9 digits)` | Covers digit-limit validation statement |
<br>


### Block Coverage Criteria

| Test ID | Input | Expected Output | Purpose |
|---|---|---|---|
| BC-1 | `8-3` | `5` | Covers binary-operation block |
| BC-2 | `-4+1` | `-3` | Covers unary negative block |
| BC-3 | `(2+3)*4` | `20` | Covers parentheses and nested expression block |
| BC-4 | `8(9)` | `72` | Covers normalization block for implicit multiplication |
<br>


### Condition Coverage Criteria

| Test ID | Input | Expected Output | Condition Exercised |
|---|---|---|---|
| CC-1 | `8/4` | `2` | Float result is integer → true |
| CC-2 | `7/2` | `3.5` | Float result is integer → false |
| CC-3 | `8(9)` | `72` | Number followed by `(` normalization → true |
| CC-4 | `(2+3)4` | `20` | `)` followed by number normalization → true |
| CC-5 | `(2+3)(4+1)` | `25` | `)` followed by `(` normalization → true |
| CC-6 | `999999999` | `999999999` | Digit count within limit → true |
| CC-7 | `1000000000` | `Error: Number too large (max 9 digits)` | Digit count over limit → false |
<br>


### Path Coverage Criteria

| Test ID | Input | Expected Output | Path Covered |
|---|---|---|---|
| PC-1 | `3*4+2` | `14` | Normal parse → evaluate → return |
| PC-2 | `-2*5` | `-10` | Unary negative → binary operation |
| PC-3 | `8(9)/7+3` | `13.285714285714286` | Normalize → parse → evaluate |
| PC-4 | `((3` | `Error` | Parse failure path |
| PC-5 | `(4+1)/(3-3)` | `Error: Divide by zero` | Parse success → runtime divide-by-zero |
| PC-6 | `1000000000+1` | `Error: Number too large (max 9 digits)` | Normalize/validate → reject before evaluation |
<br>


---



## Black-Box Testing
<br>


### Equivalence Class Partitioning (ECP)
<br>


#### Valid equivalence classes

| Test ID | Input | Expected Output | Class |
|---|---|---|---|
| ECP-V1 | `6+2` | `8` | Valid whole-number expression |
| ECP-V2 | `7/2` | `3.5` | Valid decimal result |
| ECP-V3 | `-5+3` | `-2` | Valid negative-number expression |
| ECP-V4 | `(3+5)*2` | `16` | Valid parenthesized expression |
| ECP-V5 | `8(9)` | `72` | Valid implicit multiplication expression |
| ECP-V6 | `999999999` | `999999999` | Valid 9-digit numeric input |
<br>


#### Invalid equivalence classes

| Test ID | Input | Expected Output | Class |
|---|---|---|---|
| ECP-I1 | `2+a` | `Error` | Invalid character input |
| ECP-I2 | `3*/2` | `Error` | Invalid operator sequence |
| ECP-I3 | `9/0` | `Error: Divide by zero` | Division by zero |
| ECP-I4 | `1000000000` | `Error: Number too large (max 9 digits)` | Numeric input exceeds 9-digit constraint |
<br>


### Boundary Value Analysis (BVA)

| Test ID | Input | Expected Output | Boundary Purpose |
|---|---|---|---|
| BVA-1 | `99999999` | `99999999` | Just below 9-digit limit |
| BVA-2 | `999999999` | `999999999` | Maximum valid 9-digit input |
| BVA-3 | `1000000000` | `Error: Number too large (max 9 digits)` | Just above 9-digit limit |
| BVA-4 | `999999999+1` | `1000000000` | Valid expression using max-size operand |
| BVA-5 | `1000000000+1` | `Error: Number too large (max 9 digits)` | Expression with oversized operand |
| BVA-6 | `12345.6789` | `12345.6789` | Decimal within 9 total digits |
| BVA-7 | `123456789.1` | `Error: Number too large (max 9 digits)` | Decimal exceeding 9 total digits |
