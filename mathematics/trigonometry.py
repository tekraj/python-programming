def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sine(x, terms=10):
    """Calculate sine of x using Taylor series expansion.
    sin(x) = x - (x^3/3!) + (x^5/5!) - ..........
    term(n) = (-1^n) * x ^(2n+1) / (2n+1)!  
    """
    sine_sum = 0
    for n in range(0,terms):
        sign = (-1) ** n
        sine_sum += sign * (x ** (2 * n + 1) ) / factorial(2 * n + 1)
    return sine_sum

def cosine(x, terms=10):
    """Calculate cosine of x using Taylor series expansion.
    cos(x) = 1 - (x**2/2!)+(x**4/4!)-........
    term(n) = (-1^n) * x ^2n / 2n!
    """
    cosine_sum = 0
    for n in range(0,terms):
        sign = (-1) ** n
        cosine_sum += sign * (x ** (2 * n)) / factorial(2 * n)
    return  cosine_sum

def tangent(x, terms=10):
    """Calculate tangent of x as sine(x) / cosine(x)."""
    sin_x = sine(x, terms)
    cos_x = cosine(x, terms)
    if cos_x == 0:
        raise ValueError("Tangent is undefined for this angle.")
    return sin_x / cos_x
