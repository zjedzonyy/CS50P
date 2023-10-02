def main():
    word = input("Input: ")
    new_word = shorten(word)

    print(new_word)

def shorten(word):
    new_text = ""
    skip = "AaEeIiOoUu"
    for a in word:
        if a in skip:
            continue
        else:
            new_text += a

    return new_text

if __name__ == "__main__":
    main()