import random

def main():
    level = get_level()
    problems={

    }

    for i in range(1, 10):
        x, y = generate_integer(level)
        problems[i] = {"problem" : f"{x} + {y} = ", "solution" : x + y}

    score = 1
    for i in problems:
        for j in range(1,4):
            try:
                print(problems[i]["problem"], end="")
                guess = int(input())
                result = int(problems[i]["solution"])
                if guess != result:
                    print("EEE")
                else:
                    score += 1
                    break
            except (ValueError):
                pass
            if j == 3:
                print(problems[i]["problem"], result)
                break
    print(f"Score: {score}")

def get_level():
    while True:
        level = input("Level: ")
        if level == "1" or level == "2" or level == "3":
            break
    return level


def generate_integer(level):
    x = 0
    y = 0
    if level == "1":
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == "2":
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x,y


if __name__ == "__main__":
    main()


