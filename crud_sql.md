-- CRUD SQL statements can vary based on the specific operations you want to perform. Below are examples:

-- Select all records from the Employee table
SELECT * FROM Employee;

-- Update the name of employee with EmployeeID 1
UPDATE Employee SET Name = 'Updated Name' WHERE EmployeeID = 1;

-- Insert a new employee into the Employee table
INSERT INTO Employee (EmployeeID, Name, Age, DepartmentID) VALUES (4, 'New Employee', 28,
