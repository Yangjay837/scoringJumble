
import random


word_hints = [
    ("LISTEN", "A sense organ"),
    ("SILENT", "Not making a sound"),
    ("ENLIST", "Join the military"),
    ("TINSLE", "Decorative thread"),
    ("INLET", "A narrow body of water"),

]


score = 0


def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return "".join(word_list)


def play_round():
    global score
    word, hint = random.choice(word_hints)
    jumbled_word = shuffle_word(word)
    print(f"Unscramble the letters: {jumbled_word}")
    response = input("Enter your answer (or 'hint' for a hint): ")
    if response.lower() == "hint":
        print(f"Hint: {hint}")
        response = input("Enter your answer: ")
        if response.upper() == word:
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer was {word}.")
    elif response.upper() == word:
        print("Correct!")
        score += 2
    else:
        print(f"Sorry, the correct answer was {word}.")


while True:
    play_round()
    print(f"Your current score is {score}.")
    response = input("Play again? (y/n): ")
    if response.lower()!= "y":
        break

print("Thanks for playing!")