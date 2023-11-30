CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Age INTEGER,
    DepartmentID INTEGER,
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);

CREATE TABLE IF NOT EXISTS Department (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName TEXT NOT NULL,
    HODID INTEGER,
    NumStaff INTEGER,
    FOREIGN KEY (HODID) REFERENCES Employee(EmployeeID)
);

CREATE TABLE IF NOT EXISTS Position (
    PositionID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Salary REAL,
    Description TEXT
);

CREATE TABLE IF NOT EXISTS Project (
    ProjectID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT,
    Description TEXT,
    EmployeeID INTEGER,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);
