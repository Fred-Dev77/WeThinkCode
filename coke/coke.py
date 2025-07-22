def main():
    machine()

def machine():

    coins_due = 50
    while coins_due >0:

        print(f"Amount Due: {coins_due}")

        coins = int(input('Insert Coin: '))

        if coins == 25:
            coins_due -= 25
            continue
        elif coins == 10:
            coins_due -= 10
            continue
        elif coins == 5:
            coins_due -= 5
            continue
    print(f"Change Owed: {coins_due * -1}")


main()
