
#To do program in python using List

def display_tasks(task_list):
    print("Tasks:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task}")
    print()

def add_task(task_list, new_task):
    task_list.append(new_task)
    print(f"Added '{new_task}' to the task list.\n")

def remove_task(task_list, task_index):
    if 1 <= task_index <= len(task_list):
        removed_task = task_list.pop(task_index - 1)
        print(f"Removed '{removed_task}' from the task list.\n")
    else:
        print("Invalid task index. Please enter a valid task index.\n")

def main():
    tasks = []

    while True:
        print("To Do List Program")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            display_tasks(tasks)
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            print("Quitting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    main()
