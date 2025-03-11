import tkinter as tk
from tkinter import messagebox
import json
import os

# Define Colors
BG_COLOR = "#F0F0F0"  # Light Gray
TEXT_COLOR = "#333"  # Dark Gray
BUTTON_COLOR = "#008CBA"  # Blue Buttons
BUTTON_HOVER = "#005F8C"  # Darker Blue
LISTBOX_BG = "#FFFFFF"  # White Listbox
LISTBOX_FG = "#333333"  # Dark Gray Text
FONT_STYLE = ("Arial", 12)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x550")
        self.root.config(bg=BG_COLOR)

        self.filename = "tasks.json"
        self.tasks = self.load_tasks()

        # Title Label
        self.label = tk.Label(root, text="📝 To-Do List", font=("Arial", 18, "bold"), fg=TEXT_COLOR, bg=BG_COLOR)
        self.label.pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, width=40, font=FONT_STYLE, bg="white", fg=TEXT_COLOR)
        self.task_entry.pack(pady=5)

        # Buttons Frame
        self.button_frame = tk.Frame(root, bg=BG_COLOR)
        self.button_frame.pack(pady=10)

        self.add_button = self.create_button("➕ Add Task", self.add_task)
        self.complete_button = self.create_button("✔ Mark Completed", self.mark_completed)
        self.delete_button = self.create_button("❌ Delete Task", self.delete_task)

        # Task Listbox
        self.task_listbox = tk.Listbox(root, width=50, height=10, font=FONT_STYLE, bg=LISTBOX_BG, fg=LISTBOX_FG)
        self.task_listbox.pack(pady=10)

        # Exit Button
        self.exit_button = self.create_button("🚪 Exit", root.quit)

        # Load tasks
        self.load_listbox()

    def create_button(self, text, command):
        """Creates a styled button with hover effect."""
        btn = tk.Button(self.button_frame, text=text, font=FONT_STYLE, bg=BUTTON_COLOR, fg="white",
                        command=command, width=18, relief="raised")
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Enter>", lambda e: btn.config(bg=BUTTON_HOVER))
        btn.bind("<Leave>", lambda e: btn.config(bg=BUTTON_COLOR))
        return btn

    def load_tasks(self):
        """Load tasks from a JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []

    def save_tasks(self):
        """Save tasks to a JSON file."""
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        """Add a new task."""
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.save_tasks()
            self.load_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def load_listbox(self):
        """Update the task list in the Listbox."""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            self.task_listbox.insert(tk.END, f"[{status}] {task['task']}")

    def mark_completed(self):
        """Mark the selected task as completed."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = True
            self.save_tasks()
            self.load_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed!")

    def delete_task(self):
        """Delete the selected task."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.save_tasks()
            self.load_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
