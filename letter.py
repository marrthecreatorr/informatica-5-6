def main():
    reciever = ["Mario","Luigi", "Daisy", "Yoshi", "Toad", "Princess Peach", "Bowser", "Toadette", "wario", "Waluigi", "Rosalina"]


    for letter in reciever:
        if letter != "Princess Peach":
            print(f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
       Dear {letter},

       You are cordially invited to a ball at
       Peach's Castle this evening, 7:00 PM.

       Sincerely,
       {reciever[5]}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
""")

if __name__ == "__main__":
    main()

