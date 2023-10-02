def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if 2 <= len(s) <= 6:
        for a in s[:2]:
            if not a.isalpha():
                return False
        for a in s:
            if not a.isalpha() and not a.isdigit():
                return False
        for a in s:
            if a.isdigit():
                if a != "0":
                    break
                else:
                    return False

        for i in range(len(s)):
            if s[i].isdigit() and i < len(s) - 1:
                if s[i+1].isalpha():
                    return False


        return True
    else:
        return False


if __name__ == "__main__":
    main()