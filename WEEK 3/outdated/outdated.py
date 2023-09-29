my_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        date = input("Date: ")
        m, d, y = date.split("/")
        m = int(m)
        d = int(d)
        y = int(y)
        if m < 1 or m > 12:
            continue
        if d < 1 or d > 31:
            continue
        print(f"{y:02}-{m:02}-{d:02}")

    except (ValueError):
        try:
            m, d, y = date.split()
            if not d.endswith(","):
                continue
            d = d.replace(",", "")
            m = my_list.index(m)
            d = int(d)
            y = int(y)
            m = int(m) + 1
            if m < 1 or m > 12:
                continue
            if d < 1 or d > 31:
                continue
            print(f"{y:02}-{m:02}-{d:02}")
        except (ValueError):
            pass
        else:
            break

    else:
        break


# input 1: 9/8/1636
# input 2: September 8, 1636
# output: 1636-09-08

