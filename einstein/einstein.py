def main():
    print(f"E: {emc(int(input("m: ")))}")

def emc(n):
    n = n * 300000000 ** 2
    return n

main()
