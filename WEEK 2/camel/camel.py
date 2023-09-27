text = input("camelCase: ")

new_text = ""

for a in text:
    if a.isupper():
        new_text += a.replace(a, "_")
        new_text += a.lower()
    else:
        new_text += a


print(new_text)