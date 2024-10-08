def calculator():
    operation = input("Choose an operation (+, -, *, /): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        print(f"Result: {num1 + num2}")
    elif operation == '-':
        print(f"Result: {num1 - num2}")
    elif operation == '*':
        print(f"Result: {num1 * num2}")
    elif operation == '/':
        print(f"Result: {num1 / num2}")
    else:
        print("Invalid operation")

calculator()

