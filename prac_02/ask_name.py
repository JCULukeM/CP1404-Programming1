def main():
    OUTPUT_FILE = "f:\ name.txt"
    out_file = open(OUTPUT_FILE, 'w')

    name = str(input("What is your name ma boi: "))

    print("Your name is {}! A+++ What a wonderful name you magical being!".format(name), file=out_file)
    out_file.close()
    in_file = open(OUTPUT_FILE, 'r')
    print(in_file.read())
    in_file.close()
main()
