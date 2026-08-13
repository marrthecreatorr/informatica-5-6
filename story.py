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

    name = input("What is your name? ").strip().title()
    color = input("Tell me your color: ").strip().lower()
    adjetive = input("Give me a adjetive:").strip().lower()
    goal = input("What is your goal? ").strip().lower()

    print(f"Hello, {name}!")
    print()

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adjetive}. I decided today {goal}.")


    name = input("What is your name? ").strip().upper()
    color = input("Tell me your color: ").strip().upper()
    adjetive = input("Give me a adjetive:").strip().upper()
    goal = input("What is your goal? ").strip().upper()

    print(f"Hello, {name.strip()}!")
    print()

    print("This is your story:")
    print(f"At dawn the sky turned {color}, and the air felt {adjetive}. I decided today {goal}.".strip().upper())

if __name__ == "__main__":
    main()
