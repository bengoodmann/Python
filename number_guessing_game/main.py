import random

print("Welcome to Number Guessing Game!")
print("**Easy mode** has 10 attempts and with random numbers from 1 - 15")
print("**Hard mode** has 5 attempts and with random numbers from 1 - 20")

end_game = False

while not end_game:
    mode = input("Choose a difficulty...(Type E for Easy and H for Hard)\n> ").lower()

    if mode == "e":
        attempts = 10
        print("You have 10 attempts remaining")
        random_number = random.randint(1, 15)
        while attempts != 0:
            user_guess = int(input("Guess a number between 1 and 15\n> "))
            if user_guess == random_number:
                print(f"You won! Your guess is {user_guess}")
                break
            else:
                if user_guess > random_number:
                    print("Too high!")
                elif user_guess < random_number:
                    print("Too low")
                attempts -= 1
            print(f"You have {attempts} attempts remaining")

    elif mode == "h":
        attempts = 5
        random_number = random.randint(1, 20)
        while attempts != 0:
            user_guess = int(input("Guess a number between 1 and 20\n> "))
            if user_guess == random_number:
                print(f"You won! Your guess is {user_guess}")
                break
            else:
                if user_guess > random_number:
                    print("Too high!")
                elif user_guess < random_number:
                    print("Too low")
                attempts -= 1
            print(f"You have {attempts} attempts remaining")

    else:
        print("Invalid command!")

    response = input("Do you want to continue? (Y/N)\n> ").lower()
    if response != "y":
        end_game = True
