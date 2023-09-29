
my_dict = {}
while True:
    try:
        name = input()
        name = name.upper()
        if name not in my_dict:
            my_dict[name] = 1
        else:
            my_dict[name] += 1
    except (EOFError):
        break

sorted_dict = dict(sorted(my_dict.items()))

for a in sorted_dict:
    a = a.upper()
    print(sorted_dict[a], a)



