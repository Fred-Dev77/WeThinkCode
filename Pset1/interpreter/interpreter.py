def main():
    calculate(input("Expression: "))

def calculate(expression):
    x, sign, y = expression.split(' ')
    x, y = float(x), float(y)

    if sign == '+':
        print(x + y)
    elif sign == '-':
        print(x - y)
    elif sign == '*':
        print(x * y)
    elif sign == '/':
        print(x / y)


main()
