import random
def main():

    start_game()

def start_game():
    with open("words.txt") as hangman_words:
        words = hangman_words.read().splitlines()
        guess = random.choice(words)
        print(guess)

if __name__ == "__main__":
    main()



# Define the main function
# Create txt file
# Make a list of the word we want to guess
# Open the txt file in our code
# Difine the txt file
# Add a number of tries
# Create an if function if they got it wrong or right
# If they got it correct print the whole word

