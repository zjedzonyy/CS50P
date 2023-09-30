import random

while True:
    try:
        level = input("Level: ")
        level = int(level)
        if level < 1:
            continue
        break
    except (ValueError):
        pass

u = random.randint(1, level)

while True:
    try:
        guess = input("Guess: ")
        guess = int(guess)
        if guess > u:
            print("Too large!")
            continue
        elif guess < u:
            print("Too small!")
            continue
        else:
            print("Just right!")
            break

    except (ValueError):
        pass

