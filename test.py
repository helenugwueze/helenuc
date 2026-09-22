class TaskTracker:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append({"task": description, "done": False})
        print(f"Added: '{description}'")

    def show_tasks(self):
        if not self.tasks:
            print("\nNo tasks tracked yet!")
            return
        print("\n--- Your Tasks ---")
        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task["done"] else " "
            print(f"{index}. [{status}] {task['task']}")

    def complete_task(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1]["done"] = True
            print(f"Marked task {index} as complete!")
        else:
            print("Invalid task number.")

# Quick demonstration
tracker = TaskTracker()
tracker.add_task("Learn Python loops")
tracker.add_task("Build a data app")
tracker.complete_task(1)
tracker.show_tasks()
