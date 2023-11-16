import sqlite3
from tkinter import ttk, messagebox
import tkinter as tk

# new
conn = sqlite3.connect("employee.db")
cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Employee (
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
        FOREIGN KEY (HODID) REFERENCES Employee(EmployeeID)
    )
"""
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Position (
        PositionID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL,
        Salary REAL,
        Description TEXT
    )
"""
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Project (
        ProjectID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT,
        Description TEXT,
        EmployeeID INTEGER,
        FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
    )
"""
)

cursor.execute(
    """
    CREATE TRIGGER IF NOT EXISTS UpdateNumStaff
    AFTER INSERT ON Employee
    FOR EACH ROW
    BEGIN
        UPDATE Department
        SET NumStaff = (SELECT COUNT(*) FROM Employee WHERE DepartmentID = NEW.DepartmentID),
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

emp_fields = ["EmployeeID", "Name", "Age", "DepartmentID"]
dep_fields = ["DepartmentID", "Department Name", "HODID"]
pos_fields = ["PositionID", "Title", "Salary", "Description"]
proj_fields = ["ProjectID", "Title", "Description", "EmployeeID"]


for i, field in enumerate(emp_fields, start=1):
    label = tk.Label(
        emp_form, text=f"{field}: ", font=("Roboto", 14), bg=col_4, fg=col_1
    )
    label.grid(row=i - 1, column=0, padx=(25, 5), pady=5)

emp_id_entry = tk.Entry(emp_form)
emp_id_entry.grid(row=0, column=1, columnspan=2)
name_entry = tk.Entry(emp_form)
name_entry.grid(row=1, column=1, columnspan=2)
age_entry = tk.Entry(emp_form)
age_entry.grid(row=2, column=1, columnspan=2)
department_entry = tk.Entry(emp_form)
department_entry.grid(row=3, column=1, columnspan=2)

for i, field in enumerate(dep_fields, start=1):
    label = tk.Label(
        dep_form, text=f"{field}: ", font=("Roboto", 14), bg=col_4, fg=col_1
    )
    label.grid(row=i - 1, column=0, padx=(25, 5), pady=5)

dep_id_entry = tk.Entry(dep_form)
dep_id_entry.grid(row=0, column=1, columnspan=2)
name_entry_dep = tk.Entry(dep_form)
name_entry_dep.grid(row=1, column=1, columnspan=2)
HOD_ID_entry = tk.Entry(dep_form)
HOD_ID_entry.grid(row=2, column=1, columnspan=2)

for i, field in enumerate(proj_fields, start=1):
    label = tk.Label(
        proj_form, text=f"{field}: ", font=("Roboto", 14), bg=col_4, fg=col_1
    )
    label.grid(row=i - 1, column=0, padx=(25, 5), pady=5)

proj_id = tk.Entry(proj_form)
proj_id.grid(row=0, column=1, columnspan=2)
title_proj = tk.Entry(proj_form)
title_proj.grid(row=1, column=1, columnspan=2)

description_proj = tk.Entry(proj_form)
description_proj.grid(row=2, column=1, columnspan=2)
EmpID_proj = tk.Entry(proj_form)
EmpID_proj.grid(row=3, column=1, columnspan=2)

for i, field in enumerate(pos_fields, start=1):
    label = tk.Label(
        pos_form, text=f"{field}: ", font=("Roboto", 14), bg=col_4, fg=col_1
    )
    label.grid(row=i - 1, column=0, padx=(25, 5), pady=5)

pos_id = tk.Entry(pos_form)
pos_id.grid(row=0, column=1, columnspan=2)
title_pos = tk.Entry(pos_form)
title_pos.grid(row=1, column=1, columnspan=2)

salary_pos = tk.Entry(pos_form)
salary_pos.grid(row=2, column=1, columnspan=2)
desc_pos = tk.Entry(pos_form)
desc_pos.grid(row=3, column=1, columnspan=2)


def insert_logic(selected_table):
    try:
        if selected_table == "Department":
            id_dep = int(dep_id_entry.get())
            department_name = str(name_entry_dep.get())
            hod_id = int(HOD_ID_entry.get())

            cursor.execute(
                "INSERT INTO Department(DepartmentID, DepartmentName, HODID) VALUES (?, ?, ?)",
                (id_dep, department_name, hod_id),
            )

        elif selected_table == "Employee":
            id_emp = emp_id_entry.get()
            emp_name = name_entry.get()
            emp_age = age_entry.get()
            emp_dep = department_entry.get()
            cursor.execute(
                f"INSERT INTO Employee VALUES(?, ?, ?, ?)",
                (id_emp, emp_name, emp_age, emp_dep),
            )
        elif selected_table == "Position":
            selected_table = "Position"
            id_pos = pos_id.get()
            pos_title = title_pos.get()
            pos_salary = salary_pos.get()
            pos_desc = desc_pos.get()
            cursor.execute(
                f"INSERT INTO Position VALUES(?, ?, ?, ?)",
                (id_pos, pos_title, pos_salary, pos_desc),
            )
        else:
            selected_table = "Project"
            id_proj = proj_id.get()
            project_title = title_proj.get()
            project_description = description_proj.get()
            proj_emp = EmpID_proj.get()
            cursor.execute(
                f"INSERT INTO Project VALUES(?, ?, ?, ?)",
                (id_proj, project_title, project_description, proj_emp),
            )

        messagebox.showinfo("Response", "Insertion Success")
        conn.commit()

    except Exception as e:
        messagebox.showerror("Error", f"Error during insertion: {str(e)}")


def update_logic(selected_table):
    try:
        record_id = None
        update_values = {}

        if selected_table == "Department":
            record_id = dep_id_entry.get()
            update_values["DepartmentName"] = name_entry_dep.get()
            update_values["HODID"] = HOD_ID_entry.get()
        elif selected_table == "Employee":
            record_id = emp_id_entry.get()
            update_values["Name"] = name_entry.get()
            update_values["Age"] = age_entry.get()
            update_values["DepartmentID"] = department_entry.get()
        elif selected_table == "Position":
            record_id = pos_id.get()
            update_values["Title"] = title_pos.get()
            update_values["Salary"] = salary_pos.get()
            update_values["Description"] = desc_pos.get()
        else:
            record_id = proj_id.get()
            update_values["Title"] = title_proj.get()
            update_values["Description"] = description_proj.get()
            update_values["EmployeeID"] = EmpID_proj.get()
        update_values = {
            key: value for key, value in update_values.items() if value != ""
        }
        set_clause = ", ".join(f"{key} = ?" for key in update_values.keys())

        sql_query = (
            f"UPDATE {selected_table} SET {set_clause} WHERE {selected_table}ID = ?"
        )
        param_values = tuple(update_values.values()) + (record_id,)

        cursor.execute(sql_query, param_values)

        messagebox.showinfo("Response", "Updation Success")
        conn.commit()

    except Exception as e:
        messagebox.showerror("Error", f"Error during updation: {str(e)}")


def delete_logic(selected_table):
    try:
        record_id = None
        if selected_table == "Department":
            record_id = dep_id_entry.get()
        elif selected_table == "Employee":
            record_id = emp_id_entry.get()
        elif selected_table == "Position":
            record_id = pos_id.get()
        elif selected_table == "Project":
            record_id = proj_id.get()

        if record_id is not None:
            cursor.execute(
                f"DELETE FROM {selected_table} WHERE {selected_table}ID = ?",
                (record_id,),
            )
            messagebox.showinfo("Response", "Deletion Success")
            conn.commit()
        else:
            messagebox.showwarning("Warning", "Please select a record to delete.")

    except Exception as e:
        messagebox.showerror("Error", f"Error during deletion: {str(e)}")


insert_button = tk.Button(
    frame1,
    text="Insert",
    height=1,
    width=8,
    command=lambda: insert_logic(table_var.get()),
)
update_button = tk.Button(
    frame1,
    text="Update",
    height=1,
    width=8,
    command=lambda: update_logic(table_var.get()),
)
delete_button = tk.Button(
    frame1,
    text="Delete",
    height=1,
    width=8,
    command=lambda: delete_logic(table_var.get()),
)
tree = ttk.Treeview(
    frame2, show="headings", selectmode="browse"
)
    
def join_table_view():
    global tree
    tree.grid_forget()
    cursor.execute(f"PRAGMA table_info(Employee)")
    emp_fields_info = cursor.fetchall()
    emp_field_names = [info[1] for info in emp_fields_info]

    cursor.execute(f"PRAGMA table_info(Department)")
    dep_fields_info = cursor.fetchall()
    dep_field_names = [info[1] for info in dep_fields_info]
    field_names = ["EmployeeID", "Name", "Department", "HODID"]

    tree = ttk.Treeview(
        frame2, columns=field_names, show="headings", selectmode="browse"
    )
    tree.grid(row=0, columnspan=10)

    for field in field_names:
        tree.heading(field, text=field)
        tree.column(field, width=125)

    cursor.execute(
        """SELECT Employee.EmployeeID, Employee.Name, Department.DepartmentName, Department.HODID
        FROM Employee
        INNER JOIN Department ON Employee.DepartmentID = Department.DepartmentID"""
    )
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)

def join_proj_view():
    global tree
    tree.grid_forget()
    cursor.execute(f"PRAGMA table_info(Employee)")
    emp_fields_info = cursor.fetchall()
    emp_field_names = [info[1] for info in emp_fields_info]

    cursor.execute(f"PRAGMA table_info(Project)")
    dep_fields_info = cursor.fetchall()
    dep_field_names = [info[1] for info in dep_fields_info]
    field_names = ["EmployeeID", "Name", "Project Title", "Description"]

    tree = ttk.Treeview(
        frame2, columns=field_names, show="headings", selectmode="browse"
    )
    tree.grid(row=0, columnspan=10)

    for field in field_names:
        tree.heading(field, text=field)
        tree.column(field, width=125)

    cursor.execute(
        """SELECT Employee.EmployeeID, Employee.Name, Project.Title, Project.Description
        FROM Employee
        INNER JOIN Project ON Employee.EmployeeID = Project.EmployeeID"""
    )
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)


def update_treeview(selected_table):
    global tree
    tree.grid_forget()
    cursor.execute(f"PRAGMA table_info({selected_table})")
    fields_info = cursor.fetchall()
    field_names = [info[1] for info in fields_info]

    tree = ttk.Treeview(
        frame2, columns=field_names, show="headings", selectmode="browse"
    )
    tree.grid(row=0, columnspan=10)

    for field in field_names:
        tree.heading(field, text=field)
        tree.column(field, width=125)

    cursor.execute(f"SELECT * FROM {selected_table}")
    rows = cursor.fetchall()

    for row in rows:
        tree.insert("", "end", values=row)


dep_hod_button = tk.Button(
    frame2,
    text="Employee HOD",
    height=1,
    width=16,
    command=join_table_view,
)
emp_proj_button = tk.Button(
    frame2,
    text="Employee Projects",
    height=1,
    width=16,
    command=join_proj_view,
)


def grid_buttons():
    insert_button.grid(
        row=4,
        column=0,
        pady=(30, 0),
        padx=5,
        columnspan=3,
    )
    update_button.grid(
        row=4,
        column=3,
        pady=(30, 0),
        columnspan=3,
        padx=5,
    )
    delete_button.grid(
        row=4,
        column=6,
        pady=(30, 0),
        columnspan=3,
        padx=5,
    )


def ungrid_buttons():
    insert_button.grid_forget()
    update_button.grid_forget()
    delete_button.grid_forget()


def table_choice(selected_table):
    ungrid_buttons()
    if selected_table == "Employee":
        emp_form.grid(columnspan=10)
        proj_form.grid_forget()
        pos_form.grid_forget()
        dep_form.grid_forget()
        grid_buttons()
        update_treeview(selected_table)
    elif selected_table == "Department":
        emp_form.grid_forget()
        proj_form.grid_forget()
        pos_form.grid_forget()
        dep_form.grid(columnspan=10)
        grid_buttons()
        update_treeview(selected_table)
    elif selected_table == "Position":
        emp_form.grid_forget()
        proj_form.grid_forget()
        pos_form.grid(columnspan=10)
        dep_form.grid_forget()
        grid_buttons()
        update_treeview(selected_table)
    elif selected_table == "Project":
        emp_form.grid_forget()
        proj_form.grid(columnspan=10)
        pos_form.grid_forget()
        dep_form.grid_forget()
        grid_buttons()
        update_treeview(selected_table)
    else:
        return None


def show_frame(frame):
    if frame == 1:
        frame2.grid_forget()
        frame1.grid(row=2, columnspan=10, pady=(15, 0))
        grid_buttons()
        dep_hod_button.grid_forget()
        emp_proj_button.grid_forget()
    elif frame == 2:
        frame1.grid_forget()
        frame2.grid(row=2, columnspan=10, pady=(40, 0), padx=(50, 0))
        insert_button.grid_forget()
        update_button.grid_forget()
        delete_button.grid_forget()
        dep_hod_button.grid(row=5,column=0, columnspan=5, pady=20, padx=5)
        emp_proj_button.grid(row=5,column=5, columnspan=5, pady=20, padx=5)
    else:
        frame1.grid_forget()
        frame2.grid_forget()


title_label = tk.Label(
    root,
    text="Employee Management System",
    font=("Roboto", 24, "bold"),
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

table_options = ["Employee", "Department", "Position", "Project"]
table_var = tk.StringVar(root)
table_var.set("Choose Here")
table_label = tk.Label(
    root, text="Select Table : ", bg=col_4, font=("Roboto", 12), fg=col_1
).grid(row=1, column=4, pady=10, padx=(20, 0))

table_dropdown = ttk.Combobox(
    root,
    textvariable=table_var,
    values=table_options,
    font=("Roboto", 12),
)
table_dropdown.grid(row=1, column=5, pady=10, columnspan=4)
table_dropdown.bind("<<ComboboxSelected>>", lambda event: table_choice(table_var.get()))


button1.grid(row=1, column=0, columnspan=2, padx=(20, 10))
button2.grid(row=1, column=2, columnspan=2)


root.mainloop()
cursor.close()
