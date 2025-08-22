from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    cur_font = random.choice(fonts)
    figlet.setFont(font= cur_font)

elif len(sys.argv) == 3:
    if sys.argv[1] != "-f":
        if sys.argv[1] != "--font":
            sys.exit("Invalid Usage")

    if sys.argv[2] in fonts:
        figlet.setFont(font= sys.argv[2])
    else:
        sys.exit("Invalid Usage")

else:
    sys.exit("Invalid Usage")


user = input("Input: ")

print(f"Output: {figlet.renderText(user)}")