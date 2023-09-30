import emoji
import sys

text = ""
user = input()
user = user.split()
for a in user:
     try:
        a = emoji.emojize(a, language='alias')
     except KeyError:
        pass
     a += " "
     text += a

print(f"Output: {text}")