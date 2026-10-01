def main():

    print("Times Table Generator")
    times_table = int(input("Enter a number between 1 and 10: "))

    if 1 <= times_table <= 10:

        print(f"Here is the {times_table} times table")

        for x in range(1, 11):
            answer = x * times_table
            print(f"{x} times {times_table} is {answer}")
    else:
        print("Invalid command.")
    


if __name__ == "__main__":
    main()
