def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero."

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

if __name__ == "__main__":
    print("Testing math_utils functions:")
    print("5 + 3 =", add(5, 3))
    print("5 - 3 =", subtract(5, 3))
    print("5 * 3 =", multiply(5, 3))
    print("5 / 0 =", divide(5, 0))
    print("2 ^ 3 =", power(2, 3))
    print("10 % 3 =", mod(10, 3))
