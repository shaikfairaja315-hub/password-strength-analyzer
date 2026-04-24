import re

def check_password_strength(password):
    score = 0
    suggestions = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    # Uppercase
    if re.search("[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    # Lowercase
    if re.search("[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    # Numbers
    if re.search("[0-9]", password):
        score += 1
    else:
        suggestions.append("Include numbers")

    # Special characters
    if re.search("[@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    # Strength result
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, suggestions


# User input
password = input("Enter your password: ")
strength, suggestions = check_password_strength(password)

print("Password Strength:", strength)

if suggestions:
    print("Suggestions:")
    for s in suggestions:
        print("-", s)