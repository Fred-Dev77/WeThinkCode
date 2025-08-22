def main():
    camel(input("camelCase: "))

def camel(string):
    caps = list('QWERTYUIOPLKJHGFDSAZXCVBNM')
    new_string = ""
    for char in string:
        if char in caps:
            new_string = new_string + '_' + char
        else:
            new_string += char
    if new_string[0] == '_':
        new_string = new_string.removeprefix("_")
    print(f'snake_case: {new_string.lower()}')


main()
