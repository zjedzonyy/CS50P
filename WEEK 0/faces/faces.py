
def main():
    text = input()
    c = convert(text)

    print(c)

def convert(text):


    a = text.replace(":)", "🙂")
    b = a.replace(":(", "🙁")

    return b


main()