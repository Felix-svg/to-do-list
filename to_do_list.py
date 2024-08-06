def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append({"task": task, "completed": False})
    print()


def view_tasks(tasks):
    if not tasks:
        print("No tasks to view.")
        return

    for index, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"{index + 1}. {task['task']} - {status}")
    print()


def mark_task_as_complete(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to mark as completed: ")) - 1
    try:
        if task_num < 0 or task_num > len(tasks):
            print("Invalid task number")
        tasks[task_num]["completed"] = True
    except Exception as e:
        print(f"Error: {e}")


def delete_task(tasks):
    view_tasks(tasks)
    task_num = int(input("Enter the task number to delete: ")) - 1
    try:
        if task_num < 0 or task_num > len(tasks):
            print("Invalid task number")
        tasks.pop(task_num)
    except Exception as e:
        print(f"Error: {e}")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_as_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            exit()
        else:
            print("Invalid choice. Please choose a valid option")


if __name__ == "__main__":
    main()
