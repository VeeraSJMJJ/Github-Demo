import re

def check_password_strength():
    password = input("Enter your password: ")

    # Define minimum length and regex patterns
    min_length = 8
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'[!@#$%^&*(),.?":{}|<>]', password)

    # Collect errors
    errors = []
    if len(password) < min_length:
        errors.append(f"- Minimum {min_length} characters required.")
    if not has_upper:
        errors.append("- At least one uppercase letter required.")
    if not has_lower:
        errors.append("- At least one lowercase letter required.")
    if not has_digit:
        errors.append("- At least one digit required.")
    if not has_special:
        errors.append("- At least one special character required.")

    # Show results
    if errors:
        print("\n❌ Password is weak. Please fix the following:")
        for error in errors:
            print(error)
    else:
        print("✅ Password is strong!")

# Run the checker
check_password_strength()
