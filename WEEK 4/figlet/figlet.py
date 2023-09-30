from pyfiglet import Figlet
import sys
figlet = Figlet()

if len(sys.argv) == 1:

    text = input("Input: ")
    print(figlet.renderText(text))

elif len(sys.argv) == 3 and sys.argv[2] in figlet.getFonts() and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):

    text = input("Input: ")
    figlet.setFont(font=sys.argv[2])


    print(figlet.renderText(text))

else:
    sys.exit("Must provide 0 or 2 command line argument")
