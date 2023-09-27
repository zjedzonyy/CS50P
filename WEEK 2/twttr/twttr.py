
text = input("Input: ")
new_text = ""
skip = "AaEeIiOoUu"
for a in text:
    if a in skip:
        continue
    else:
        new_text += a

print(new_text)