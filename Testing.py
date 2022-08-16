def get_string(m, _min=2, _max=15):
    getting = True
    while getting is True:
        my_string = input(m)
        if len(my_string) < _min:
            print("Your entry is too short, please try again: ")
        elif len(my_string) >= _max:
            print("Your entry is too long, please try again: ")
        else:
            return my_string


def get_integer(m, _min=0, _max=10):
    getting = True
    while getting is True:
        try:
            my_integer = int(input(m))
        except ValueError:
            print("You have not entered a valid integer. Please try again: ")
            continue
        if my_integer < _min:
            print("Your input is too small, please try again. ")
        elif my_integer >= _max:
            print("Your input is too large, please try again.")
        else:
            return my_integer


def print_pasta(l):
    for x in l:
        output = "{} : ${}".format(x[0], x[1])
        print(output)
    print("-" * 100)


def print_with_indexes(l):
    for i in range(0, len(l)):
        output = "{} : {} : ${} : {} in your current order".format(i, l[i][0], l[i][1], l[i][2])
        print(output)


def add_pasta(l, o):
    print_with_indexes(l)
    choice = get_integer("What pasta index number would you like to add to your order? ", 0, len(l))
    quantity = get_integer("How many would you like to add to your order? ", 0, 500)
    l[choice][2] += quantity
    o.append(l[choice])
    output = "You have added {} {} to your order.".format(quantity, l[choice][0])
    print(output)


def review_order(l):
    total = 0
    for x in l:
        output = "{} : {} : ${}.".format(x[2], x[0], x[1])
        print(output)
        total += x[1] * x[2]
    print("The total cost of our order is ${}.".format(total))


def remove_pasta(o):
    view = get_string("Would you like to view your order? (y/n): ")
    if view == "y":
        review_order(o)
    choice = get_integer("What index number would you like to remove? ")
    o.pop(choice)
    output = 'You have removed the index number {} from your order'.format(choice)
    print(output)


def main():
    pasta_menu = [["Fettuccine Carbonara", 20, 0],
                  ["Spaghetti Pomodoro", 16, 0],
                  ["Ravioli di Ricotta ", 20, 0]]
    order_list = []
    run = True
    while run is True:
        # Things to print out
        # menu
        menu = '''
            P: Print out menu
            A: Add item to order
            O: Review order
            R: Remove item from order
            Q: Quit'''
        print(menu)
        choice = get_string("What would you like to do?", 1, 2)
        if choice == "P":
            print_pasta(pasta_menu)
        elif choice == "A":
            add_pasta(pasta_menu, order_list)
        elif choice == "Q":
            run = False
        elif choice == "O":
            review_order(order_list)
        elif choice == "R":
            remove_pasta(order_list)
        else:
            print("You did not enter a valid entry, please try again: ")


main()
