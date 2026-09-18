def main():
    tasks = [] #empty list

    while True:
        print(f"Tasks to do: {len(tasks)}")
        print(tasks)

        command = input("what do you want to do? (add, complete, prioritize, exit): ")
        if command == "add":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
        elif command == "Complete":
            comp_task = input("Which task did you complete?: ")
            task.remove(comp_task)
        elif command == "prioritize":
            pri_task = input("What task do you want to prioritize?: ")
            tasks.insert(0,pri_task)
        elif command == "exit":
            print("ByeBye")
            break

if __name__ == "__main__":
    main()
