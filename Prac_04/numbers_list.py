
def first_last_list(number_list):
    print ("The first number is {}".format(number_list[0]))
    print ("The last number is {}".format(number_list[-1]))


def list_average(number_list):
    list_length  = len(number_list)
    average = sum(number_list) / list_length
    print ("The average is {}".format(average))

def main():
    integer = 0
    count_number = 5
    number_list = []
    while count_number >0:
        count_number -= 1
        integer = input ("Choose a number")
        number_list.append(integer)
    print (number_list)
    first_last_list(number_list)

    print ("The smallest number is {}".format(min(number_list)))
    print ("The largest number is {}".format(max(number_list)))
    list_average(number_list)
main()