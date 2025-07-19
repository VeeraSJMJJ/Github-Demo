# Even or Odd Checker

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    print("🔍 Even or Odd Number Checker")

    # Step 1: Check a single number
    try:
        single_number = int(input("Enter a number to check if it's even or odd: "))
        print(f"{single_number} is {check_even_odd(single_number)}.\n")
    except ValueError:
        print("❌ Please enter a valid integer.\n")
        return

    # Step 2: Check a list of numbers
    number_list = input("Enter a list of numbers separated by commas: ")

    try:
        # Convert input to a list of integers
        numbers = [int(n.strip()) for n in number_list.split(',')]
        print("\n📋 Results:")
        for num in numbers:
            print(f"{num} is {check_even_odd(num)}")
    except ValueError:
        print("❌ Invalid input in the list. Please enter only integers separated by commas.")

if __name__ == "__main__":
    main()