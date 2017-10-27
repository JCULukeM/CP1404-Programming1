
def calculate_pyramid(rows):
    blocks = rows
    while rows > 0:
        blocks += rows
        calculate_pyramid(rows -1)
        print(blocks)
    return blocks


def main():
    rows = int(input("How many rows"))
    calculate_pyramid(rows)
    print("blocks")


main()
