import sqlite3
from tkinter import ttk
import tkinter as tk

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INTEGER PRIMARY KEY,
        FirstName TEXT,
        LastName TEXT,
        DateOfBirth DATE,
        PhoneNumber TEXT
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Departments (
        DepartmentID INTEGER PRIMARY KEY,
        DepartmentName TEXT
    )
"""
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS EmployeePositions (
        PositionID INTEGER PRIMARY KEY,
        PositionTitle TEXT,
        Salary REAL
    )
"""
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS EmployeeAssignments (
        AssignmentID INTEGER PRIMARY KEY,
        EmployeeID INTEGER,
        DepartmentID INTEGER,
        PositionID INTEGER,
        StartDate DATE,
        EndDate DATE,
        FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID),
        FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID),
        FOREIGN KEY (PositionID) REFERENCES EmployeePositions(PositionID)
    )
"""
)
conn.commit()

col_4 = "#363062"
col_3 = "#435585"
col_2 = "#818FB4"
col_1 = "#F5E8C7"

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - 700) // 2
y = (screen_height - 610) // 2

root.geometry(f"500x500+{x}+{y}")
root.configure(bg=col_4)
root.minsize(550, 500)
root.title("Employee Management System")


def show_frame(frame):
    frame.tkraise()


frame1 = tk.Frame(root, bg=col_4)
frame2 = tk.Frame(root, bg=col_4)
frame3 = tk.Frame(root, bg=col_4)
frame4 = tk.Frame(root, bg=col_4)

frame1.grid(row=2, columnspan=4)
frame2.grid(row=2, columnspan=4)
frame3.grid(row=2, columnspan=4)
frame4.grid(row=2, columnspan=4)


title_label = tk.Label(
    root,
    text="Employee Management System",
    font=("Roboto", 32, "bold"),
    bg=col_4,
    fg=col_1,
    anchor="center",
    justify="center",
)
title_label.grid(row=0, column=0, columnspan=10, pady=16, padx=10)
button1 = tk.Button(
    root,
    text="Insert Data",
    height=2,
    width=10,
    command=lambda: [show_frame(frame1), root.geometry(f"500x500+{x}+{y}")],
)
button2 = tk.Button(
    root,
    text="Update Data",
    height=2,
    width=10,
    command=lambda: [show_frame(frame2), root.geometry(f"500x500+{x}+{y}")],
)
button3 = tk.Button(
    root,
    text="Delete Data",
    height=2,
    width=10,
    command=lambda: [show_frame(frame3), root.geometry(f"725x550+{x}+{y}")],
)

button4 = tk.Button(
    root,
    text="Delete Data",
    height=2,
    width=10,
    command=lambda: [show_frame(frame4), root.geometry(f"500x500+{x}+{y}")],
)

button1.grid(row=1, column=0, columnspan=2, padx=(10, 0))
button2.grid(row=1, column=2, columnspan=2)
button3.grid(row=1, column=4, columnspan=2)
button4.grid(row=1, column=6, columnspan=2)


label_frame1 = tk.Label(
    frame1, text="Content for Button 1", bg=col_4, font=("Roboto", 24)
)
label_frame1.grid(row=1, columnspan=4, pady=10)

label_frame2 = tk.Label(
    frame2, text="Content for Button 2", bg=col_4, font=("Roboto", 24)
)
label_frame2.grid(row=1, columnspan=4, pady=10)

label_frame3 = tk.Label(
    frame3, text="Content for Button 3", bg=col_4, font=("Roboto", 24)
)
label_frame3.grid(row=1, columnspan=4, pady=10)

label_frame4 = tk.Label(
    frame4, text="Content for Button 4", bg=col_4, font=("Roboto", 24)
)
label_frame4.grid(row=1, columnspan=4, pady=10)


root.mainloop()
cursor.close()
