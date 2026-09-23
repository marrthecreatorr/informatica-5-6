def main ():
    answer = int(intup("Give me a numer 1-10"))
    tables = [1,2,3,4,5,6,7,8,9,10]

    if answer <= 10:
        print(f"Here is the {answer} times tables")
        for i in range (1,11):

            result = i * answer
            print(f"{i} times {answer} is {result}")
    elif answer > 10:
        print("Kay so i said 1-10")







If __name__ == "__main__":
    main()
