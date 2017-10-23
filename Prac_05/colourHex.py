
COLOUR_NAMES = {"aliceBlue": "fof8ff", "AntiqueWhite": "fa4bd7", "aquamarine1": "7ffd4", "black": "000000",
                "chartreuse1": "7fff00", "red": "ff6663", "blue": "ff6ooo"}


def main():
    colour = input("Choose a colour: ")
    while colour != "":
        print("{} is {}".format(colour, COLOUR_NAMES.get(colour)))
        colour = input("Choose a colour: ")

main()