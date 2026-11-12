
import string
import random

common_passwords = ["password", "123456", "qwerty", "admin", "12345678"]

def check_password(password):

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    print("\n--- Password Analysis ---")

    if password.lower() in common_passwords:
        print("Warning: This is a common weak password.")
        print("Strength: Weak")
        return

    if score <= 2:
        print("Strength: Weak")
    elif score <= 4:
        print("Strength: Medium")
    else:
        print("Strength: Strong")

    print("Score:", score, "/ 5")

    if suggestions:
        print("\nSuggestions:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("Your password is strong and secure!")


def generate_password():

    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""

    for i in range(12):
        password += random.choice(characters)

    print("\nGenerated Password:", password)


while True:

    print("\n===== PASSWORD SECURITY ANALYZER =====")
    print("1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        password = input("Enter your password: ")
        check_password(password)

    elif choice == "2":
        generate_password()

    elif choice == "3":
        print("Thank you for using Password Security Analyzer!")
        break

    else:
        print("Invalid choice. Please try again.")
