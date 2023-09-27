

amount = 50
owed = 0
while amount > 0:
    print(f"Amount Due: {amount}")
    coin = int(input("Insert Coin: "))
    if coin == 5:
        amount = amount - coin
    elif coin == 10:
        amount = amount - coin
    elif coin == 25:
        amount = amount - coin

amount = abs(amount)
print(f"Change Owed: {amount}")

