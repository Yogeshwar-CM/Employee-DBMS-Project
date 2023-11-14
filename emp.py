import sqlite3
from tkinter import ttk
import tkinter as tk

conn = sqlite3.connect("employee.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Employees (
        EmployeeID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Age INTEGER,
        DepartmentID INTEGER,
        FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
    )
"""
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Department (
        DepartmentID INTEGER PRIMARY KEY,
        DepartmentName TEXT NOT NULL,
        HODID INTEGER,
        NumStaff INTEGER,
        FOREIGN KEY (HODID) REFERENCES Employees(EmployeeID)
    )
"""
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Positions (
        PositionID INTEGER PRIMARY KEY,
        Title TEXT NOT NULL,
        Salary REAL,
        Description TEXT
    )
"""
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Projects (
        ProjectID INTEGER PRIMARY KEY,
        Title TEXT,
        Description TEXT,
        EmployeeID INTEGER,
        FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID)
    )
"""
)

cursor.execute(
    """
    CREATE TRIGGER IF NOT EXISTS UpdateNumStaff
    AFTER INSERT ON Employees
    FOR EACH ROW
    BEGIN
        UPDATE Department
        SET NumStaff = (SELECT COUNT(*) FROM Employees WHERE DepartmentID = NEW.DepartmentID),
            HODID = NEW.EmployeeID
        WHERE DepartmentID = NEW.DepartmentID;
    END;
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

root.geometry(f"610x500+{x}+{y}")
root.configure(bg=col_4)
root.minsize(550, 500)
root.title("Employee Management System")


frame1 = tk.Frame(root, bg=col_4)
frame2 = tk.Frame(root, bg=col_4)

emp_form = tk.Frame(frame1, bg=col_4)
dep_form = tk.Frame(frame1, bg=col_4)
proj_form = tk.Frame(frame1, bg=col_4)
pos_form = tk.Frame(frame1, bg=col_4)

cursor.execute("SELECT DepartmentID, DepartmentName FROM Department")
department_values = cursor.fetchall()
cursor.execute("SELECT EmployeeID, Name FROM Employees")
employee_values = cursor.fetchall()

emp_fields = ["Name", "Age", "DepartmentID"]
dep_fields = ["Department Name", "HODID"]
pos_fields = ["Title", "Salary", "Description"]
proj_fields = ["Title", "Description", "EmployeeID"]


for i, field in enumerate(emp_fields, start=1):
    label = tk.Label(emp_form, text=f"{field}: ", font=("Roboto", 16), bg=col_4)
    label.grid(row=i - 1, column=0, padx=(25, 5), pady=5)

name_entry = tk.Entry(emp_form)
name_entry.grid(row=0, column=1, columnspan=2)
age_entry = tk.Entry(emp_form)
age_entry.grid(row=1, column=1, columnspan=2)
department_entry = tk.Entry(emp_form)
department_entry.grid(row=2, column=1, columnspan=2)

for i, field in enumerate(dep_fields, start=1):
    label = tk.Label(dep_form, text=f"{field}: ", font=("Roboto", 16), bg=col_4)
    label.grid(row=i - 1, column=0, padx=(25, 5), pady=5)

name_entry_dep = tk.Entry(dep_form)
name_entry_dep.grid(row=0, column=1, columnspan=2)
department_entry_dep = tk.Entry(dep_form)
department_entry_dep.grid(row=1, column=1, columnspan=2)

for i, field in enumerate(proj_fields, start=1):
    label = tk.Label(proj_form, text=f"{field}: ", font=("Roboto", 16), bg=col_4)
    label.grid(row=i - 1, column=0, padx=(25, 5), pady=5)

name_entry_asn = tk.Entry(proj_form)
name_entry_asn.grid(row=0, column=1, columnspan=2)

age_entry_asn = tk.Entry(proj_form)
age_entry_asn.grid(row=1, column=1, columnspan=2)
department_entry_asn = tk.Entry(proj_form)
department_entry_asn.grid(row=2, column=1, columnspan=2)

for i, field in enumerate(pos_fields, start=1):
    label = tk.Label(pos_form, text=f"{field}: ", font=("Roboto", 16), bg=col_4)
    label.grid(row=i - 1, column=0, padx=(25, 5), pady=5)

name_entry_pos = tk.Entry(pos_form)
name_entry_pos.grid(row=0, column=1, columnspan=2)

age_entry_pos = tk.Entry(pos_form)
age_entry_pos.grid(row=1, column=1, columnspan=2)
department_entry_pos = tk.Entry(pos_form)
department_entry_pos.grid(row=2, column=1, columnspan=2)



def table_choice(selected_table):
    if selected_table == "Employees":
        emp_form.grid()
        proj_form.grid_forget()
        pos_form.grid_forget()
        dep_form.grid_forget()
        return 1
    elif selected_table == "Departments":
        emp_form.grid_forget()
        proj_form.grid_forget()
        pos_form.grid_forget()
        dep_form.grid()
        return 2
    elif selected_table == "EmployeePositions":
        emp_form.grid_forget()
        proj_form.grid_forget()
        pos_form.grid()
        dep_form.grid_forget()
        return 3
    elif selected_table == "EmployeeAssignments":
        emp_form.grid_forget()
        proj_form.grid()
        pos_form.grid_forget()
        dep_form.grid_forget()
        return 4
    else:
        return None


def show_frame(frame):
    if frame == 1:
        frame1.grid(row=2, columnspan=10, pady=(15, 0))
        frame2.grid_forget()
    elif frame == 2:
        frame2.grid(row=2, columnspan=10, pady=(15, 0))
        frame1.grid_forget()
    else:
        frame1.grid_forget()
        frame2.grid_forget()


title_label = tk.Label(
    root,
    text="Employee Management System",
    font=("Roboto", 32, "bold"),
    bg=col_4,
    fg=col_1,
    anchor="center",
    justify="center",
)
title_label.grid(row=0, column=0, columnspan=10, pady=16, padx=(20, 0))
button1 = tk.Button(
    root,
    text="Modify Data",
    height=2,
    width=10,
    command=lambda: [show_frame(1)],
)
button2 = tk.Button(
    root,
    text="View Data",
    height=2,
    width=10,
    command=lambda: [show_frame(2)],
)

table_options = ["Employees", "Departments", "EmployeePositions", "EmployeeAssignments"]
table_var = tk.StringVar(root)
table_var.set("Choose Here")
table_label = tk.Label(
    root, text="Select Table : ", bg=col_4, font=("Roboto", 16), fg=col_1
).grid(row=1, column=4, pady=10)

table_dropdown = ttk.Combobox(
    root,
    textvariable=table_var,
    values=table_options,
    font=("Roboto", 14),
)
table_dropdown.grid(row=1, column=5, pady=10, columnspan=4)
table_dropdown.bind("<<ComboboxSelected>>", lambda event: table_choice(table_var.get()))


button1.grid(row=1, column=0, columnspan=2, padx=(16, 0))
button2.grid(row=1, column=2, columnspan=2)


root.mainloop()
print(table_choice())
cursor.close()
