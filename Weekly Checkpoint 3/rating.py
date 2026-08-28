def main():
    print("Thank you for visiting the cinema! leave a rating")

    rating = float(input("Leave a reating 0-5:"))

    if rating > 4.5:
        print("Perfection")
    elif rating > 4:
        print("Excellent")
    elif rating > 3:
        print("Good")
    elif rating > 2:
        print("Fair")
    else:
        print("Poor")

if __name__ == "__main__":
    main()

