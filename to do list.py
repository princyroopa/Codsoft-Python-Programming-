class ToDoListApp:
    def __init__(self):
        self.tasks = []
    
    def display_menu(self):
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
    
    def add_task(self):
        task = input("Enter the task description: ")
        self.tasks.append({'task': task, 'completed': False})
        print(f"Task '{task}' added.")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        
        print("\nYour To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            status = "Completed" if task['completed'] else "Pending"
            print(f"{i}. {task['task']} - {status}")
    
    def mark_task_completed(self):
        self.view_tasks()
        try:
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_index < len(self.tasks):
                self.tasks[task_index]['completed'] = True
                print(f"Task '{self.tasks[task_index]['task']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    def delete_task(self):
        # Delete a task
        self.view_tasks()
        try:
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(self.tasks):
                print(f"Task '{self.tasks[task_index]['task']}' deleted.")
                del self.tasks[task_index]
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.mark_task_completed()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    app = ToDoListApp()
    app.run()
