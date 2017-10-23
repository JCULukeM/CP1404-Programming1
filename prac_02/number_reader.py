
def main():
    total = 0
    INPUT_FILE = "f:/numbers.txt"
    in_file = open(INPUT_FILE, 'r')
    for num in in_file:
        new_num = num.strip("\n")
        total = int(new_num)+ total
        print(new_num,end = " ")

    print('\n',total)
    in_file.close()
main()