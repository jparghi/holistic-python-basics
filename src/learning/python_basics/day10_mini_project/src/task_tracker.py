"""
Title: Task Tracker
Objective: Manage a list of tasks with completion status.
Date: 2024-06-07
"""

tasks: list[dict[str, bool]] = []

while True:
    print("\nTask Tracker")
    print("1. Add task")
    print("2. Complete task")
    print("3. View tasks")
    print("4. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        description = input("Task description: ")
        tasks.append({"description": description, "done": False})
        print("Task added!")
    elif choice == "2":
        if not tasks:
            print("No tasks to complete.")
            continue
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "⬜"
            print(f"{index}. {status} {task['description']}")
        selection = int(input("Enter the number of the task to complete: "))
        if 1 <= selection <= len(tasks):
            tasks[selection - 1]["done"] = True
            print("Task marked as complete!")
        else:
            print("Invalid selection.")
    elif choice == "3":
        if not tasks:
            print("No tasks recorded yet.")
        else:
            print("\nCurrent tasks:")
            for index, task in enumerate(tasks, start=1):
                status = "✅" if task["done"] else "⬜"
                print(f"{index}. {status} {task['description']}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Please choose a valid option.")
