def check_password(password):
    length = len(password)

    digits = sum(char.isdigit() for char in password)
    upper = sum(char.isupper() for char in password)
    lower = sum(char.islower() for char in password)
    special = sum(not char.isalnum() for char in password)

    if length >= 8 and digits >= 1 and upper >= 1 and lower >= 1 and special >= 1:
        print("Strong Password ")
    elif length >= 6 and digits >= 1 and upper >= 1:
        print("Moderate Password ")
    else:
        print("Weak Password ")

password = input("Enter your password: ")
check_password(password)