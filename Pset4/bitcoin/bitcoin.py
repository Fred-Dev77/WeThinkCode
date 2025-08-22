import sys
import requests
import json

try:
    if len(sys.argv) != 2:
        print("missing command-line argument")
        sys.exit(1)
    else:
        num = float(sys.argv[1])

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

answer = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

rate = answer["bpi"]["USD"]["rate"]
amount = num * rate

print(f"${amount:,.4f}")

