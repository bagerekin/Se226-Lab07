import math_utils

def main():
    try:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return

    op = input("Enter operator (+, -, *, /, ^, %): ").strip()
    operations = {
        '+': math_utils.add,
        '-': math_utils.subtract,
        '*': math_utils.multiply,
        '/': math_utils.divide,
        '^': math_utils.power,
        '%': math_utils.mod
    }

    if op not in operations:
        print("Invalid operator.")
        return

    try:
        result = operations[op](x, y)
    except Exception as e:
        print(f"Error during operation: {e}")
        return

    if isinstance(result, str):
        print(result)
    else:
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
