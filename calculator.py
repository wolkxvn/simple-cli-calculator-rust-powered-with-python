import calc_backend

def main():
    print("Simple Calculator")
    print("Operations: add, subtract, multiply, divide")
    print("Type 'exit' to quit")

    while True:
        operation = input("Enter operation: ").strip()
        if operation == 'exit':
            break

        if operation not in ['add', 'subtract', 'multiply', 'divide']:
            print("Invalid operation. Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if operation == 'add':
            result = calc_backend.add(a, b)
        elif operation == 'subtract':
            result = calc_backend.subtract(a, b)
        elif operation == 'multiply':
            result = calc_backend.multiply(a, b)
        elif operation == 'divide':
            try:
                result = calc_backend.divide(a, b)
            except ZeroDivisionError:
                print("Error: Division by zero.")
                continue

        print(f"Result: {result}")

if __name__ == '__main__':
    main()
