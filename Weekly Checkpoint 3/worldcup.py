def main():
    spain = int(input("Spain goals: "))
    argentina = int(input("Argentina goal: "))

    if spain > argentina:
        print("Spain is the champion!")

    elif argentina > spain:
        print("Argentina is the winner!")

    else:
        print("Its a tie.")

    print("gg")

if __name__ == "__main__":
    main()
