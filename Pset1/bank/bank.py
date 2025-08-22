def main():
    bank(input('Greeting: '))

def bank(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        print("$0")
    elif "how" in greeting:
        print("$20")
    elif "hey" in greeting:
        print("$20")
    else:
        print("$100")


main()
