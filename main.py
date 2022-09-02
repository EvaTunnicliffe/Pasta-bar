def get_string(m, _min=2, _max=15):
    """
    Validation for string inputs

    :param m: string
    :param _min: Shortest string possible
    :param _max: Longest string possible
    :return: string
    """

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
    """
        Validation for integer inputs

        :param m: integer
        :param _min: Smallest integer possible
        :param _max: Largest integer possible
        :return: integer
        """
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
    """
    Printing out the pasta menu
    :param l: list  (pasta list)
    """
    for x in l:
        output = "{} which is {} : ${}".format(x[0], x[3], x[1])
        print(output)
    print(" ")


def print_with_indexes(l):
    """
    Printing out the pasta menu with index numbers
        :param l: list  (pasta list)
    """
    for i in range(0, len(l)):
        output = "{} : {} : ${} each : You currently have {} in your order".format(i, l[i][1], l[i][2], l[i][0])
        print(output)
    print(" ")


def add_pasta(l, o):
    """
    Function for adding pasta to the customers order

    :param l: list  (pasta list)
    :param o: list  (customer order list)

    """
    print_with_indexes(l)
    choice = get_integer("What pasta index number would you like to add to your order? ", 0, len(l))
    quantity = get_integer("How many would you like to add to your order? ", 1, 6)
    pasta_name = l[choice][0]
    pasta_price = l[choice][1]

    o.append([quantity, pasta_name, pasta_price])
    output = "You have added {} {} to your order that costs ${} each.".format(quantity, l[choice][0], l[choice][1])
    print(output)


def review_order(o):
    """
    Function for reviewing the customers order

    :param o: list  (customer order list)

    """
    total = 0
    for x in o:
        output = "{} : {} : ${}.".format(x[0], x[1], x[2])
        print(output)
        total += x[0] * x[2]
    print("The total cost of our order is ${}.".format(total))


def remove_pasta(o):
    """
    Function for removing a type of pasta from the customers order

        :param o: list  (customer order list)

        """
    print_with_indexes(o)
    chose = True
    while chose is True:
        choice = get_integer("What index number would you like to remove? ")
        if choice in range(0, len(o)):
            o.pop(choice)
            output = 'You have removed the index number {} from your order'.format(choice)
            print(output)
            chose = False
        else:
            print("You have not entered a valid input, please try again")
            chose = True


def edit_order(o):
    """
    Function for editing the customers order

        :param o: list  (customer order list)

        """
    print_with_indexes(o)
    edit = True
    while edit is True:
        option = get_integer("What index number would you like to edit? ")
        if option in range(0, len(o)):
            output = "You currently have {} {} in your order. ".format(o[option][0], o[option][1])
            print(output)
            new_value = get_integer("How many would you like to have now? ")
            o[option][0] = new_value
            edit = False
        else:
            print("You have not entered a valid input, please try again")
            edit = True


def get_details(d, o):
    """
    Function for asking the customer all of their details, and if they would like delivery or pick up

        :param d: list  (customer detail list)
        :param o: list  (customer order list)

        """
    name = get_string("Can you please enter your name -> ", 0, 50)
    phone = get_string("Can you please enter your phone number -> ", 0, 15)
    options = ["D : Delivery", "P : Pick Up"]
    for x in options:
        print(x)
    user_choice = get_string("Please enter your choice, "
                             "there is a $3 extra charge for delivery services -> ", 0, 2).upper()
    if user_choice == "D":
        o.append([1, "Delivery fee", 3])
        delivery = True
        while delivery is True:
            number = get_integer("Can you please enter the number of your address -> ", 0, 50)
            street = get_string("Can you please enter your street name -> ", 0, 50)
            suburb = get_string("Can you please enter the suburb you live in -> ", 0, 50)
            city = get_string("Can you please enter the city that you live in -> ", 0, 50)
            post_code = get_string("Can you please enter your post code -> ", 0, 6)
            address = "{} {}, {}, {}, {}".format(number, street, suburb, city, post_code)
            confirmation = get_string("Your address is {}. Is this correct? Y or N: ".format(address), 0, 2).upper()
            if confirmation == "Y":
                output = "Name: {}, Phone Number: {}, Address: {}".format(name, phone, address)
                d.extend([name, phone, address])
                print(output)
                delivery = False
            elif confirmation == "N":
                delivery = True
            else:
                print("Sorry, you have entered an invalid input. Please try again: ")
                delivery = True

    elif user_choice == "P":
        print("You have selected pick up")
        output = "Name: {}, Phone Number: {}".format(name, phone)
        d.extend([name, phone])
        print(output)


def final_order(o, c):
    """
    Function for letting the user finalise their order and their details

        :param o: list  (customer order list)
        :param c: list  (customer detail list)
        :return: none

        """
    total = 0
    for x in o:
        output = "You currently have {} {} in your order. This costs ${} each. ".format(x[0], x[1], x[2])
        print(output)
        total += x[0] * x[2]
    output = "Your current order is ${} in total.".format(total)
    print(output)
    if len(c) == 2:
        output = "Your customer details are currently {}, {}, your order is for a pick-up".format(c[0], c[1])
        print(output)
    elif len(c) == 3:
        output = "Your customer details are currently {}, {}, " \
                 "and your address for delivery is {}. ".format(c[0], c[1], c[2])
        print(output)
    else:
        print("Sorry, the customer details have not been entered correctly, please try again. ")
    correct = True
    while correct is True:
        ask = get_string("Are these details correct? Y/N: ", 0, 2).upper()
        if ask == "Y":
            order_or_quit = order_again(o, c)
            return order_or_quit
        elif ask == "N":
            print("You will now be returned to the main menu, please enter your customer details again. ")
            return True
        else:
            print("Incorrect entry, please try again.")
            correct = True


def order_again(o, c):
    """
    Function for user to start a new order or not

           :param o: list  (customer order list)
           :param c: list  (customer detail list)

           """
    ordering = True
    while ordering is True:
        again = get_string("Would you like to place another order? Y/N: ", 0, 2).upper()
        if again == "Y":
            print("Your first order has been submitted and will be ready in 20 minutes. "
                  "Continue to place another order. ")
            o.clear()
            c.clear()
            return True
        elif again == "N":
            print("Thank you for ordering a meal, it will be ready in 20 minutes.")
            return False
        else:
            print("Incorrect entry, please try again.")
            ordering = True


def main():
    """
    Function to guide the user through the process of ordering at the 1154 pasta bar.
    """
    pasta_menu = (("Fettuccine Carbonara", 20, 0, "Long, flat pasta. Creamy egg and pepper sauce, bacon, parmesan."),
                  ("Spaghetti Pomodoro", 16, 0, "Long, thin pasta. Classic tomato and basil sauce, parmesan."),
                  ("Ravioli di Ricotta ", 20, 0,
                   "Spinach and ricotta (filled) pasta, brown butter sauce, sage, hazelnuts, parmesan. "),
                  ("Linguine Gamberi", 23, 0,
                   "Long flat pasta. Tomato, garlic and chilli sauce, prawns anchovies, capers, olives, parmesan."),
                  ("Fusili Pesto", 19, 0,
                   "Short, spiral pasta. Kale and cashew pesto and cream sauce, olives, parmesan."),
                  ("Rigatoni alla Caponata", 21, 0,
                   "Short, tube pasta. Agrodolce tomato sauce, eggplant, ricotta salata, pine nut."),
                  ("Vegan Pomodoro", 16, 0, "Vegan pasta with tomato and herb sauce, nutritional yeast."),
                  ("Conchilglie alla Bolognese", 22, 0,
                   "Small, shell pasta. Northern italian beef and pork sauce, parmesan."))
    order_list = []
    customer_details = []
    run = True
    while run is True:
        # Things to print out
        # menu
        menu = '''
            P: Print out menu
            A: Add item to order
            R: Review order
            D: Remove item from order
            E: Edit Order
            C: Get Customer details
            F: Finalise Order
            Q: Quit'''
        print(menu)
        choice = get_string("What would you like to do? ", 1, 2).upper()
        print(" ")
        if choice == "P":
            print_pasta(pasta_menu)
        elif choice == "A":
            add_pasta(pasta_menu, order_list)
        elif choice == "Q":
            run = False
        elif choice == "R":
            review_order(order_list)
        elif choice == "D":
            remove_pasta(order_list)
        elif choice == "E":
            edit_order(order_list)
        elif choice == "C":
            get_details(customer_details, order_list)
        elif choice == "F":
            run = final_order(order_list, customer_details)
        else:
            print("You did not enter a valid entry, please try again: ")


main()
