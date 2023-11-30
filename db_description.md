# Database Description

## Tables

### Employee

| Attribute | Data Type | Description | Primary Key | Foreign Key |
|-----------|-----------|-------------|-------------|-------------|
| EmployeeID | INTEGER | Unique identifier for each employee | Yes | No |
| Name | TEXT | Name of the employee | No | No |
| Age | INTEGER | Age of the employee | No | No |
| DepartmentID | INTEGER | Department to which the employee belongs | No | Yes |

### Department

| Attribute | Data Type | Description | Primary Key | Foreign Key |
|-----------|-----------|-------------|-------------|-------------|
| DepartmentID | INTEGER | Unique identifier for each department | Yes | No |
| DepartmentName | TEXT | Name of the department | No | No |
| HODID | INTEGER | EmployeeID of the Head of Department | No | Yes |
| NumStaff | INTEGER | Number of employees in the department | No | No |

### Position

| Attribute | Data Type | Description | Primary Key | Foreign Key |
|-----------|-----------|-------------|-------------|-------------|
| PositionID | INTEGER | Unique identifier for each position | Yes | No |
| Title | TEXT | Title of the position | No | No |
| Salary | REAL | Salary associated with the position | No | No |
| Description | TEXT | Description of the position | No | No |

### Project

| Attribute | Data Type | Description | Primary Key | Foreign Key |
|-----------|-----------|-------------|-------------|-------------|
| ProjectID | INTEGER | Unique identifier for each project | Yes | No |
| Title | TEXT | Title of the project | No | No |
| Description | TEXT | Description of the project | No | No |
| EmployeeID | INTEGER | EmployeeID of the employee responsible for the project | No | Yes |

## Constraints

### Primary Key Constraints

Each table has a primary key constraint that ensures each row has a unique identifier.

### Foreign Key Constraints

The Department table has a foreign key constraint that references the Employee table. This ensures that the HODID (Head of Department) attribute in the Department table must be a valid EmployeeID.

The Employee table has a foreign key constraint that references the Department table. This ensures that the DepartmentID attribute in the Employee table must be a valid DepartmentID.

The Project table has a foreign key constraint that references the Employee table. This ensures that the EmployeeID attribute in the Project table must be a valid EmployeeID.

### Referential Integrity Constraints

The foreign key constraints enforce referential integrity, ensuring that the data in the database is consistent.

## Normalization

The database is in Third Normal Form (3NF). This means that the data is organized in a way that minimizes redundancy and ensures that all non-prime attributes are dependent on the primary key.

## Sample Data

### Employee

| EmployeeID | Name        | Age | DepartmentID |
|------------|-------------|-----|--------------|
| 1          | John Doe     | 30  | 1            |
| 2          | Jane Smith   | 25  | 2            |
| 3          | Peter Jones  | 40  | 3            |

### Department

| DepartmentID | DepartmentName | HODID | NumStaff |
|--------------|-----------------|-------|----------|
| 1            | IT              | 1     | 3        |
| 2            | Sales           | 2     | 2        |
| 3            | HR              | 3     | 1        |

### Position

| PositionID | Title              | Salary | Description                            |
|------------|--------------------|--------|----------------------------------------|
| 1          | Software Engineer  | 100000 | Develops and maintains software applications |
| 2          | Sales Manager       | 120000 | Manages a team of sales representatives |
| 3          | HR Manager          | 150000 | Manages human resources activities    |

### Project

| ProjectID | Title                   | Description                              | EmployeeID |
|-----------|-------------------------|------------------------------------------|------------|
| 1         | E-commerce Website      | Develop a new e-commerce website for the company | 1          |
| 2         | CRM System               | Implement a new CRM (Customer Relationship Management) system | 2          |
| 3         | Employee Training Program| Develop and implement a new employee training program | 3          |
