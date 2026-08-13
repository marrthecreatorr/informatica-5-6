def main():
    # planet = input("Planet:")

    # # Separation
    # print("Hello",planet)

    # # Concatenation
    # print("Hello " + planet)

    # # Formatted Strings
    # print(f"Hello {planet}")

    # # Ending
    # print("Hello", end=" ")
    # print(planet)

    name = input("What is your name? ")
    color = input("Tell me your color: ")
    adjetive = input("Give me a adjetive:")
    goal = input("What is your goal? ")

    print(f"Hello, {name}!")
    print()

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adjetive}. I decided today {goal}.")


if __name__ == "__main__":
    main()
