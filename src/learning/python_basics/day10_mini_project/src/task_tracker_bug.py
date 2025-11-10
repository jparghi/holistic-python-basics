"""
Title: Task Tracker (Buggy)
Objective: Provide list and loop errors for debugging practice.
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
        task = {"description": description, "done": False}
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "⬜"
            print(f"{index}. {status} {task['description']}")
        selection = int(input("Enter the number of the task to complete: "))
        tasks[selection]["done"] = True
        print("Task marked as complete!")
    elif choice == "3":
        print("\nCurrent tasks:")
        for index, task in enumerate(tasks, start=1):
            status = "✅" if task["done"] else "⬜"
            print(f"{index}. {status} {task['description']}")
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Please choose a valid option.")
