while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        result = x / y * 100
        if result > 100:
            print("WRONG")
            continue

    except (TypeError, ValueError, ZeroDivisionError, NameError):
        print("WRONG")

    else:
        break


if result <= 1:
    print("E")
elif result >= 99:
    print("F")
else:
    print(f"{round(result)}%")


