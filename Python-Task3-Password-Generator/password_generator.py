# Password Generator
# Asks for the length and character types, then generates a random password.

import secrets

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITS = "0123456789"
SYMBOLS = "!@#$%^&*()-_=+?"


def ask_yes_no(message):
    # Keep asking until the user types y or n
    while True:
        answer = input(message).strip().lower()
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Please type y or n.")


def get_length():
    # Keep asking until the user types a whole number between 4 and 64
    while True:
        text = input("Password length (4-64): ").strip()
        if text.isdigit() and 4 <= int(text) <= 64:
            return int(text)
        print("Enter a whole number between 4 and 64.")


def has_any(password, characters):
    # True if the password contains at least one character from the given set
    for letter in password:
        if letter in characters:
            return True
    return False


def make_password(length, groups):
    # Join all chosen groups into one string of allowed characters
    allowed = ""
    for group in groups:
        allowed = allowed + group

    # Build passwords until one contains a character from every chosen group
    while True:
        password = ""
        for i in range(length):
            password = password + secrets.choice(allowed)

        all_groups_used = True
        for group in groups:
            if not has_any(password, group):
                all_groups_used = False

        if all_groups_used:
            return password


# ---------- Main program ----------
length = get_length()

while True:
    groups = []
    if ask_yes_no("Include lowercase letters? (y/n): "):
        groups.append(LOWERCASE)
    if ask_yes_no("Include uppercase letters? (y/n): "):
        groups.append(UPPERCASE)
    if ask_yes_no("Include digits? (y/n): "):
        groups.append(DIGITS)
    if ask_yes_no("Include symbols? (y/n): "):
        groups.append(SYMBOLS)

    if len(groups) == 0:
        print("Choose at least one type.")
    elif length < len(groups):
        print("Length is too short for the chosen types.")
        length = get_length()
    else:
        break

print()
print("Your password:", make_password(length, groups))
