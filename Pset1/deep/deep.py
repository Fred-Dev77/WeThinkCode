def main():
    deep(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))

def deep(question):
    question = question.strip()
    if question.lower() == "forty two" or question.lower() == "forty-two" or question.lower() == "42":
        print("yes")
    else:
        print("no")

main()
