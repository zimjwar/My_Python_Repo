# Basic arithmetic functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return "Undefined (cannot divide by zero)" if y == 0 else x / y

def exponent(x, y):
    return x ** y

def modulus(x, y):
    return "Undefined (cannot mod by zero)" if y == 0 else x % y
