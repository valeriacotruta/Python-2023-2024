def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        if b == 0:
            raise Exception("Division by 0!")
    except Exception as e:
        return e
    else:
        return a / b
