def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    b = d.replace("$", "")
    dollars = float(b)

    return dollars


def percent_to_float(p):
    c = p.replace("%", "")
    percent = float(c)
    percent = percent/100

    return percent

main()