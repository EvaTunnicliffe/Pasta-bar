def get_string(m):
    my_string = input(m)
    return my_string


def get_integer(m):
    my_integer = input(m)
    return my_integer


def print_pasta(l):
    for x in l:
        output = "{} : {}".format(x[0], x[1])
        print(output)
        print("-"*100)


def main():
    pasta_menu = [["Fettuccine Carbonara", 20],
                  ["Spaghetti Pomodoro", 16],
                  ["Ravioli di Ricotta", 20]]
    run = True
    while run is True:
        # Things to print out
        # menu
        menu = '''
        P: Print out menu
        Q: Quit'''
        print(menu)
        choice = input("What would you like to do? ")
        if choice == "P":
            print_pasta(pasta_menu)
        elif choice == "Q":
            run = False


main()
