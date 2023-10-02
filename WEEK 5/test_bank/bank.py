
def main():
    text = input("Greeting: ")
    text = text.lower()
    result = value(text)

    print(f"${result}")

def value(greeting):
    if "hello" in greeting:
        return 0
    elif "h" == greeting[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()