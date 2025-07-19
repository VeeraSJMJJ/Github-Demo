def age_category(age):
    if age < 0:
        return "Invalid age"
    elif age <= 1:
        return "Baby"
    elif age <= 3:
        return "Infant"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

# Ask user for age input
try:
    age = float(input("Enter your age in years: "))
    category = age_category(age)
    print(f"You are classified as a: {category}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
