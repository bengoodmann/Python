from data import data
from art import logo, vs
from secrets import choice
from os import system


print(logo)


point = 0
wrong = False
b = choice(data)
while not wrong:
    print(logo)
    a = b

    while a["name"] == b["name"]:
        b = choice(data)

    print(f"{a['name']}, {a['description']}, from {a['country']}")
    print(vs)
    print(f"{b['name']}, {b['description']}, from {b['country']}")
    user_response = input("Who has more followers?(A or B)\n> ").lower()

    a_follower_count = int(a["follower_count"])
    b_follower_count = int(b["follower_count"])
    system("cls")
    if user_response in ["a", "b"]:
        if a_follower_count > b_follower_count and user_response == "a":
            point += 1
            print(f"You're right! Your current score is {point}")
        elif b_follower_count > a_follower_count and user_response == "b":
            point += 1
            print(f"You're right! Your current score is {point}")
        else:
            print(f"Sorry, that's wrong. Your final score is {point}")
            wrong = True
    else:
        print("You chose the wrong word!")
