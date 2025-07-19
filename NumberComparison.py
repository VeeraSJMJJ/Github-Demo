def compare_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if num1 > num2:
            print(f"{num1} is larger than {num2}")
        elif num1 < num2:
            print(f"{num1} is smaller than {num2}")
        else:
            print(f"Both numbers are equal ({num1} = {num2})")
    except ValueError:
        print("❌ Please enter valid numbers.")

# Run the comparison
compare_numbers()
