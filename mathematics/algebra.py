import math

def nth_root(value, n):
    if value < 0 and n % 2 == 0:
        raise ValueError("Cannot compute the even root of a negative number.")
    return value ** (1 / n)

def solve_quadratic_eq(a, b, c):
    """Solve a quadratic equation ax^2 + bx + c = 0 using the quadratic formula.
       Returns two roots as a tuple."""
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        raise ValueError("No real roots.")
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    return root1, root2

