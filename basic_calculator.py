# Simple Calculator for Two Numbers

def calculator():
    print("🔢 Welcome to the Simple Calculator")

    # Input two numbers
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform the operation
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("❌ Error: Division by zero is not allowed.")
            return
        result = num1 / num2
    else:
        print("❌ Invalid operator. Please use +, -, *, or /.")
        return

    # Output the result
    print(f"✅ Result: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()