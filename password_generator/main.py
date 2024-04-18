import string
import secrets
import random


alpha = string.ascii_letters
number = string.digits
special_char = string.punctuation

print("Welcome to Uniq Password Generator")
password_list = []
name_of_password = input(
    "What's the name of the password? eg. Facebook, Twitter\n> "
).lower()
number_of_letters = int(input("How long do you want the password to be?\n> "))
number_of_numbers = int(input("How many numbers do you want in your password?\n> "))
number_of_special = int(input("How many special characters do you want?\n> "))


if number_of_letters > (number_of_numbers + number_of_special):
    for char in range(0, number_of_letters - (number_of_numbers + number_of_special)):
        password_list.append(secrets.choice(alpha))

    for num in range(0, number_of_numbers):
        password_list.append(secrets.choice(number))

    for num in range(0, number_of_special):
        password_list.append(secrets.choice(special_char))

    password = ""

    random.shuffle(password_list)

    for c in password_list:
        password += c

    password_file = [
        {name_of_password: password}
    ]

    print(f"Your password is {password}")

    filepath = "password.txt"

    with open(file=filepath, mode="a+") as f:
        f.write(f"{password_file}\n")

else:
    print("Length of number and special characters is higher than length of password!")
