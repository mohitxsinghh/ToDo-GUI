import tkinter as tk  # Import the Tkinter library for creating the GUI
from tkinter import messagebox  # Import messagebox for displaying alerts
import json  # Import JSON for task persistence

# Define the main class for the To-Do List Application GUI
class ToDoAppGUI:
    def __init__(self, root):
        # Initialize the root window
        self.root = root
        self.root.title("To-Do List Application")  # Set the window title
        
        self.file_name = 'tasks.json'  # Define the file name for task storage
        self.tasks = self.load_tasks()  # Load tasks from the JSON file

        # --- GUI Elements Setup ---
        # Task List (Listbox to display tasks)
        self.task_listbox = tk.Listbox(self.root, height=10, width=50)  # Create a Listbox widget
        self.task_listbox.pack(pady=10)  # Pack the Listbox into the window with padding

        # Task input fields
        # Create and pack a Label and Entry for task title
        self.title_label = tk.Label(self.root, text="Task Title:")  # Create label for task title
        self.title_label.pack()  # Pack the label
        self.title_entry = tk.Entry(self.root, width=40)  # Create an Entry widget for task title input
        self.title_entry.pack()  # Pack the entry field

        # Create and pack a Label and Entry for task description
        self.desc_label = tk.Label(self.root, text="Task Description:")  # Create label for task description
        self.desc_label.pack()  # Pack the label
        self.desc_entry = tk.Entry(self.root, width=40)  # Create an Entry widget for task description input
        self.desc_entry.pack()  # Pack the entry field

        # Create and pack a Label and Entry for task category
        self.cat_label = tk.Label(self.root, text="Category:")  # Create label for task category
        self.cat_label.pack()  # Pack the label
        self.cat_entry = tk.Entry(self.root, width=40)  # Create an Entry widget for task category input
        self.cat_entry.pack()  # Pack the entry field

        # Buttons
        # Create and pack an 'Add Task' button
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)  # Button to add a new task
        self.add_button.pack(pady=5)  # Pack the button with padding

        # Create and pack a 'Mark as Completed' button
        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_completed)  # Button to mark task as completed
        self.complete_button.pack(pady=5)  # Pack the button with padding

        # Create and pack a 'Delete Task' button
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)  # Button to delete selected task
        self.delete_button.pack(pady=5)  # Pack the button with padding

        # Load tasks from file and display them in the Listbox
        self.update_task_listbox()

    # Load tasks from the JSON file
    def load_tasks(self):
        try:
            # Try to open the tasks file and load the tasks into the list
            with open(self.file_name, 'r') as file:
                return json.load(file)  # Return the list of tasks
        except (FileNotFoundError, json.JSONDecodeError):
            # If file is not found or there is an error in JSON, return an empty list
            return []

    # Save the tasks back to the JSON file
    def save_tasks(self):
        with open(self.file_name, 'w') as file:
            json.dump(self.tasks, file, indent=4)  # Dump tasks with indentation for readability

    # Update the Listbox to display the current list of tasks
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Clear the current Listbox items
        # Iterate through tasks and add each one to the Listbox
        for idx, task in enumerate(self.tasks):
            status = 'Completed' if task['completed'] else 'Pending'  # Check if task is completed or pending
            # Create a formatted string for each task to display in the Listbox
            task_str = f"{idx + 1}. [{status}] {task['title']} ({task['category']})"
            self.task_listbox.insert(tk.END, task_str)  # Insert task string into the Listbox

    # Add a new task to the list
    def add_task(self):
        title = self.title_entry.get()  # Get the task title from the input field
        description = self.desc_entry.get()  # Get the task description
        category = self.cat_entry.get()  # Get the task category

        # Ensure all fields are filled
        if title and description and category:
            # Create a new task dictionary
            new_task = {
                'title': title,
                'description': description,
                'category': category,
                'completed': False  # Task is not completed by default
            }
            self.tasks.append(new_task)  # Add the new task to the tasks list
            self.save_tasks()  # Save tasks to the JSON file
            self.update_task_listbox()  # Update the Listbox to show the new task
            self.clear_input_fields()  # Clear the input fields
        else:
            # Show a warning if any field is empty
            messagebox.showwarning("Input Error", "Please fill all fields.")

    # Mark the selected task as completed
    def mark_completed(self):
        selected_index = self.task_listbox.curselection()  # Get the index of the selected task
        if selected_index:
            task_idx = selected_index[0]  # Get the index of the task
            self.tasks[task_idx]['completed'] = True  # Mark the task as completed
            self.save_tasks()  # Save tasks to the JSON file
            self.update_task_listbox()  # Update the Listbox to show the updated task
        else:
            # Show a warning if no task is selected
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    # Delete the selected task
    def delete_task(self):
        selected_index = self.task_listbox.curselection()  # Get the index of the selected task
        if selected_index:
            task_idx = selected_index[0]  # Get the index of the task
            self.tasks.pop(task_idx)  # Remove the task from the list
            self.save_tasks()  # Save the updated task list to the JSON file
            self.update_task_listbox()  # Update the Listbox to reflect the deleted task
        else:
            # Show a warning if no task is selected
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    # Clear the input fields after a task is added
    def clear_input_fields(self):
        self.title_entry.delete(0, tk.END)  # Clear the task title input field
        self.desc_entry.delete(0, tk.END)  # Clear the task description input field
        self.cat_entry.delete(0, tk.END)  # Clear the task category input field

# Running the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the root Tkinter window
    app = ToDoAppGUI(root)  # Initialize the To-Do App GUI
    root.mainloop()  # Start the Tkinter event loop (keeps the window open)
