import requests
import sys


try:
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    number = float(sys.argv[1])
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    r = r.json()
    price = r["bpi"]['USD']['rate_float'] * number


except (ValueError):
    print("Command-line argument is not a number")
    sys.exit(1)

print(f"${price:,.4f}")