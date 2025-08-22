def main():
    print(convert(input()))

def convert(text):
    text = text.replace(":)","\N{slightly smiling face}")
    text = text.replace(":(","\N{slightly frowning face}")
    return text

main()
