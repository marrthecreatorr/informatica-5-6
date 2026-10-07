def main():

    welcome()
    get_item()


def welcome():
    menu = ("Cheeseburger", "Fries", "Soda", "Ice Cream", "Cookie")
    print("Welcome to marburgers!!!")
    print("Here's the menu:")
    for i in range(len(menu)):
        print(f"{i+1} {menu[i]}")

def get_item():
    


if __name__ == "__main__":
    main()
