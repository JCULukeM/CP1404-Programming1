from random import randint


def num_generator(lottery_list, number_quick_picks):
    num = 90
    line_len = 6
    for i in range(0, number_quick_picks):
        while line_len > 0:
            num = randint(1, 45)
            if num not in lottery_list:
                lottery_list.append(num)
                line_len -= 1
        lottery_list.sort()
        print(lottery_list)
        del lottery_list[:]
        line_len = 6
        number_quick_picks - 1


def main():
    lottery_list = []
    number_quick_picks = int(input("How many quick picks"))
    num_generator(lottery_list, number_quick_picks)


main()
