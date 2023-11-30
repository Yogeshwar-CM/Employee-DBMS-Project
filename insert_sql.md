-- Sample data for Employee table
INSERT INTO Employee (EmployeeID, Name, Age, DepartmentID) VALUES
(1, 'John Doe', 30, 1),
(2, 'Jane Smith', 25, 2),
(3, 'Peter Jones', 40, 3);

-- Sample data for Department table
INSERT INTO Department (DepartmentID, DepartmentName, HODID, NumStaff) VALUES
(1, 'IT', 1, 3),
(2, 'Sales', 2, 2),
(3, 'HR', 3, 1);

-- Sample data for Position table
INSERT INTO Position (PositionID, Title, Salary, Description) VALUES
(1, 'Software Engineer', 100000, 'Develops and maintains software applications'),
(2, 'Sales Manager', 120000, 'Manages a team of sales representatives'),
(3, 'HR Manager', 150000, 'Manages human resources activities');

-- Sample data for Project table
INSERT INTO Project (ProjectID, Title, Description, EmployeeID) VALUES
(1, 'E-commerce Website', 'Develop a new e-commerce website for the company', 1),
(2, 'CRM System', 'Implement a new CRM (Customer Relationship Management) system', 2),
(3, 'Employee Training Program', 'Develop and implement a new employee training program', 3);
