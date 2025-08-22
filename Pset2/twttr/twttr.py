def main():
    remove_vowel(input("Input: "))

def remove_vowel(string):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    print(new_string)


main()
