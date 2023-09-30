import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        if name:
            names.append(name)
        else:
            break

    except (EOFError):
        break


text = p.join(names)

print("")
print(f"Adieu, adieu, to {text}")
