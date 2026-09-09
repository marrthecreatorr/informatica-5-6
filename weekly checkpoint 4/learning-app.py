import random

def main():
    print("Welcome to duo app")

    n1 = random.randint(10,99)
    n2 = random.randint(10,99)


    answer = n1 + n2
    guess = 0

    while guess != answer:
    print(f"What is:{n1} + {n2}?")
    guess = int(input("Your answer:"))


if __name__ == "__main__":
    main()
