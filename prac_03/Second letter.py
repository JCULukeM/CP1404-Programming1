
def print_second_letter(name,letters):
    for i in range(0, len(name),letters):
        print(name[i], end='')


def main():
    name = input("What is your name: ")
    letters = int(input("Which letters?: "))
    print_second_letter(name,letters)


main()
