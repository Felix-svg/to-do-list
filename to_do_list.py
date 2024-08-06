def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task():
    pass


def view_tasks():
    pass


def mark_task_as_complete():
    pass


def delete_task():
    pass


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            mark_task_as_complete()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please choose a valid option")

if __name__ == "__main__":
    main()
