def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    num = ''
    s = s.upper()
    letters = list("QWERTYUIOPASDFGHJKLZXCVBNM")
    numbers = list("0987654321")
    punctuation = list(" !@#$%^&*()_+=-|]}[{:;/?.>,<`~'")
    if 2 < len(s) <= 6:
        for char in s:
            if char in punctuation:
                return False
            if char in numbers:
                num += char
                if num[0] == "0":
                    return False
                if s[-1:] in letters:
                    return False
                if s[-2:-1] in letters:
                    return False

        for chars in s[0:2]:
            if chars not in letters:
                return False

        return True


    else:
        return False


main()
