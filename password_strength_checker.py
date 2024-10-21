import re

def check_password_strength(password):
    # Initialize strength variables
    length_check = len(password) >= 8
    upper_check = re.search(r'[A-Z]', password) is not None
    lower_check = re.search(r'[a-z]', password) is not None
    digit_check = re.search(r'\d', password) is not None
    special_check = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Count the number of criteria met
    strength_score = sum([length_check, upper_check, lower_check, digit_check, special_check])

    # Determine password strength
    if strength_score == 5:
        return "Strong password"
    elif strength_score >= 3:
        return "Moderate password"
    else:
        return "Weak password"

# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")
