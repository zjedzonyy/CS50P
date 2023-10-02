
def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    result = gauge(percentage)

    print(result)

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    percentage = round(x / y * 100)


    return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()