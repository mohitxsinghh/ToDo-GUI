# ToDo-GUI
# To-Do List Application

A simple, GUI-based To-Do List application built with Python's Tkinter library for task management, including functionality to add, delete, complete tasks, and categorize them. Task data is persisted locally using a JSON file.

## Features

- **Add Task:** Add new tasks with a title, description, and category.
- **Complete Task:** Mark tasks as completed.
- **Delete Task:** Remove tasks from the list.
- **Categorization:** Organize tasks by category.
- **Local Persistence:** Tasks are saved in a `tasks.json` file for later retrieval.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
  
## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/todo-app.git
    ```
2. Navigate to the project directory:
    ```bash
    cd todo-app
    ```
3. Install the required dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```

   > **Note:** There are no external dependencies in this project except Python’s standard libraries (`tkinter` and `json`).

## Usage

1. Run the application:
    ```bash
    python todo_app.py
    ```

2. The GUI window will open, allowing you to:
   - Add new tasks by filling in the title, description, and category fields.
   - Mark tasks as completed by selecting the task and clicking "Mark as Completed".
   - Delete tasks by selecting the task and clicking "Delete Task".

3. All tasks will be saved in the `tasks.json` file and reloaded when you run the app again.

## File Structure

```plaintext
todo-app/
│
├── tasks.json             # JSON file for storing tasks
├── todo_app.py            # Main Python application
└── README.md              # Project documentation
