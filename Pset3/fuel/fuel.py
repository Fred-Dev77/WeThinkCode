def main():
    fuel()

def fuel():
    while True:
        fraction = input("Fraction: ")

        try:
            n, d = fraction.split("/")
            n = int(n.strip())
            d = int(d.strip())
            percent = int(round(n / d * 100))
        except (ValueError, ZeroDivisionError):
            continue



        if 5 > percent >= 0:
            print("E")
        elif 95 >= percent >= 5:
            print(f"{percent}%")
        elif 95 < percent <= 100:
            print("F")
        else:
            continue
        break




main()
