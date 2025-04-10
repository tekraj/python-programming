def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def exponentiate(a, b):
    return a ** b

def modulus(a, b):
    return a % b

def floor_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b
