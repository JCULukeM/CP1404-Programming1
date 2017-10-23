from random import randint


def num_generator(lottery_list, number_quick_picks):
    line_len = 6
    for i in range (number_quick_picks):
        while line_len > 0:
            num = randint(0, 45)
            lottery_list.append(num)
            line_len - 1
            print(lottery_list)
        number_quick_picks - 1

def main():
    lottery_list = []
    number_quick_picks = int(input("How many quick picks"))
    num_generator(lottery_list, number_quick_picks)


main()
