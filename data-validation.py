def main():
    name = True
    while name:
        try:
            namename = input("Enter a name: ")

            print(f"Stored name: {namename}")
            break

        except IndexError:
            enter = print(namename[0])
            if name == enter:
                print("Enter a name: ")

    not_validated = True # Initialization

    while not_validated: # Condition
        try:
            number = int(input("Enter a number between 1 and 10: "))
            if number < 1:
                not_validated

            elif number <= 10:
                not_validated = False
        except ValueError:
            print("You must enter a number between 1 and 10. ")


if __name__ == "__main__":
    main()
