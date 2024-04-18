import random

word_list = ["hello", "world", "welcome", "man", "dive"]
chosen_word = random.choice(word_list)

display: list = []

for _ in chosen_word:
    display.append("_")

game_over = False
game_life = ["❤️", "❤️", "❤️", "❤️", "❤️", "❤️"]

player_name = input("What's your name?\n> ")
print(
    f"Hello, {player_name}! Welcome to Hangman.\nYou have 6 game lives ❤️. You will lose a game life whenever you guess the wrong letter.\n\tHappy playing"
)
print(display)

while not game_over:
    guess = input("Guess a letter from the random word\n> ").lower()

    for n in range(len(chosen_word)):
        letter = chosen_word[n]
        if letter == guess:
            display[n] = letter

    if guess not in chosen_word:
        game_life.pop()
        print(f"Your game life {game_life}")

    if len(game_life) < 1:
        game_over = True
        print("You've used all your game life! 😒")

    if "_" not in display:
        game_over = True
        print("You win! 🎊")
    print(display)
