def count_number_types_from_input():
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = list(map(float, user_input.strip().split()))

        positives = 0
        negatives = 0
        zeros = 0

        for num in numbers:
            if num > 0:
                positives += 1
            elif num < 0:
                negatives += 1
            else:
                zeros += 1

        print("\n📊 Count Summary:")
        print(f"✅ Positive numbers: {positives}")
        print(f"🔻 Negative numbers: {negatives}")
        print(f"⭕ Zeros: {zeros}")

    except ValueError:
        print("❌ Invalid input. Please enter numbers separated by spaces.")

# Run the function
count_number_types_from_input()
