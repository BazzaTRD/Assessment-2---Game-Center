#Sanjith Padmadas Das 8/28/2025 3:40 PM • # CRUD - Create/Read/Update/Delete

tasks = []

def add_task():
    task = input("Please enter a task")
    if task:
        tasks.append(task)

def update_task():
    id = int(input("Enter the id to update the task"))
    task = input("Enter the updated task")
    tasks[id - 1] = task
    print("Task updated successfully")


def delete_task():
    id = int(input("Enter the id to delete the task"))
    tasks.pop(id - 1)
    print("Task deleted successfully")


def list_tasks():
    print("*" * 20)
    print("Your task list..")
    print("*" * 20)
    for i, task in enumerate(tasks):
        print(f"{i + 1}. {task}")
        print("*" * 20)


while True:
    print("1. Add new task")
    print("2. Update task")
    print("3. Delete task")
    print("4. Show my tasks")
    print("5. Exit")

    option = int(input("Enter you option"))

    if option == 1:
        add_task()
    elif option == 2:
        update_task()
    elif option == 3:
        delete_task()
    elif option == 4:
        list_tasks()
    elif option == 5:
        break
