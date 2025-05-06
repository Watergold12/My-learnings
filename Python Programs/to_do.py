class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done":False})

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks, start = 1):
                status = "Done" if task["done"] else "Not Done"
                print(f"{i}. {task['task']} ({status})")

    def mark_task_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["done"] = True
            print(f"Task {task_index} marked as done.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print(f"Task {task_index} deleted.")
        else:
            print("Invalid task index.")

    def save_tasks(self, filename):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']}|{task['done']}\n")
    
    def load_tasks(self, filename):
        self.tasks = []
        try:
            with open(filename, "r") as file:
               for line in file:
                task, done = line.strip().split("|")
                self.tasks.append({"task" : task, "done" : done == "True"})
                print(f"Loaded {len(self.tasks)} tasks from {filename}.")
        except  FileNotFoundError:
                print(f"File {filename} not found.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter Task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as done: "))
            todo_list.mark_task_done(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            filename = int(input("Enter filename to save tasks: "))
            todo_list.save_tasks(filename)
        elif choice == "6":
            filename = int(input("Enter filename to load tasks: "))
            todo_list.load_tasks(filename)
        elif choice == "7":
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid choice. Please try Again.")

if __name__ == "__main__":
    main()