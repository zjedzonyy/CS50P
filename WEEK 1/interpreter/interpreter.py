expression = input("Expression: ")

x, y, z = expression.split(" ")

x = float(x)
z = float(z)

if y == "+":
    r = x + z
elif y == "-":
    r = x - z
elif y == "/":
    r = x / z
else:
    r = x * z

print(r)
