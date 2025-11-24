import re

# Main function
def main():
    while True:  # loop to allow repeated input until strong and not leaked
        user_password = input("Enter a password: ")  
        strength = check_password_strength(user_password)
        print("Password strength:", strength)

        if password_leak(user_password):
            print("This password was found in a breach list!")
        else:
            print("Password not found in breach list")

        # exit loop if strong and not leaked
        if strength == "Strong" and not password_leak(user_password):
            break
        print("INPUT PASSWORD AGAIN")

# Password strength checker
def check_password_strength(password):
    score = 0

    # Length Checker
    if len(password) >= 8:
        score += 1
    else:
        print("Password length needs to be 8 characters or longer")


    # Consecutive character check
    if re.search(r"(.)\1", password):
        print("Password cannot have consecutive repeated characters")
        return "Weak"  # fail immediately


    # Includes At Least One Uppercase Letter Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        print("Password Requires At Least One Uppercase Letter")

    # Includes At Least One Lowercase Letter Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        print("Password Requires At Least One Lowercase Letter")

    # Checks If Includes At Least One Digit
    if re.search(r"[0-9]", password):
        score += 1
    else:
        print("Password Requires At Least One Number")

    # Checks If At Least One Special Character Check
    if re.search(r"[@$!%*?&#]", password):
        score += 1
    else:
        print("Password Requires At Least One Special Character")

    # Conditionals To Check If Strong Enough Score
    if score <= 2:
        return "Weak"
    elif score in (3, 4):
        return "Medium"
    else:
        return "Strong"

# Checks If Password Has Been In Password Leak
def password_leak(password):
    with open("passwords.txt", "r") as file:
        password_list = file.read().splitlines()
    return password in password_list

# Only run main if this file is executed directly
if __name__ == "__main__":
    main()
