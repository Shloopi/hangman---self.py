guessed_letter = input("Enter your guess (letter): ").lower()

if len(guessed_letter) > 1 and not guessed_letter.isalpha(): # if the input is not a single letter and not an alphabet.
    print("E3")
elif len(guessed_letter) > 1: # if the input is not a single letter.
    print("E1")
elif not guessed_letter.isalpha(): # if the input is not an alphabet.
    print("E2")
else: # otherwise, the input is valid.
    print(guessed_letter)