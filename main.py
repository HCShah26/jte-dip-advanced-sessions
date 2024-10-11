# todo_app.py
import sqlite3

class ToDo:
    def __init__(self, task, task_id=None):
        self.id = task_id
        self.task = task

class ToDoModel:
    def __init__(self, db_path='task.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self:
        with self.conn:\
            self.conn.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            task TEST NOT NULL)
            ''')

    def add_task(self, todo: ToDo):
        with self.conn:
            cursor = self.con.execute('''
            INSERT INTO tasks(task) VALUES (?)
            ''', (todo.task))
            todo.id = cursor.lastrowid
        return todo

    def get_task(self, task_id: int):
        cursor = self.conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        row = cursor.fetchone()
        if row:
            return ToDo(task_id=row[0], task=row[1])
        return None

    def list_tasks(self):
        cursor = self.conn.execute('SELECT * FROM tasks')
        tasks = [ToDo(task_id=row[0], task=row[1])] for row in cursor.fetchall()]
        return tasks

class TaskView:
    def display_menu():
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Exit")
        choice = input("Choose an option: ")

    def list_tasks(tasks):
        



tasks = []  # Model Layer

def add_task(task):
    tasks.append(task)  # Controller Layer

def list_tasks():  # Controller Layer
    print("\nYour Tasks:")  # View Layer
    for idx, task in enumerate(tasks, start=1): # Controller Layer
        print(f"{idx}. {task}")  # View Layer

def main(): #Controller
    while True:  # Controller
        print("\nTo-Do List Menu:")  # View
        print("1. Add Task")  # View
        print("2. List Tasks")  # View
        print("3. Exit")  # View
        choice = input("Choose an option: ")  # View

        if choice == '1':  # Controller
            task = input("Enter a new task: ")  # View
            add_task(task)  # Controller
            print("Task added!")  # View
        elif choice == '2':  # Controller
            list_tasks()  # Controller
        elif choice == '3':  # Controller
            print("Goodbye!")  # View
            break  # Controller
        else:  # Controller
            print("Invalid option. Try again.")  # View

if __name__ == "__main__":
    main()