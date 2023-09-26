def main():
    time = input("What time is it? ")
    time = convert(time)

    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 13.00 <= time <= 14.00:
        print("lunch time")
    elif 18.00 <= time <= 19.99:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = (float(minutes)) / 60

    time = hours + minutes


    return (time)


if __name__ == "__main__":
    main()


