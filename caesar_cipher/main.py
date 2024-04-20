from string import ascii_letters as alphabet


def caesar(direction, text, shift):
    _text = ""
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            if direction == "encode":
                index = (index + shift) % 26
                _text += alphabet[index]
            elif direction == "decode":
                index = (index - shift) % 26
                _text += alphabet[index]

    print(f"Your {direction}d text is {_text}")


end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n> ").lower()
    text = input("Type your message:\n> ").lower()
    shift = int(input("Type the shift number:\n> "))

    if direction in ["encode", "decode"]:
        caesar(direction=direction, text=text, shift=shift)
    else:
        end = True

    restart = input("Do you want to continue?(Yes or No)\n> ").lower()
    if restart == "no":
        end = True
        print("Goodbye")