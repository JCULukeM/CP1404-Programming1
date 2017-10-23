

def main():
    total = 0
    num_items = -1
    while num_items < 0:
        num_items = int(input("Number of items: "))
        if num_items < 0:
            print("Invalid number")
    item_num = num_items
    while num_items > 0:
            item = float(input("Price of item: "))
            total += item
            num_items -= 1
       
    print ("Total price for", item_num, "items", total)

main()



