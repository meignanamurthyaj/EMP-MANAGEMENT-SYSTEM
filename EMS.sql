CREATE DATABASE employee_db;

Use employee_db;

CREATE TABLE employee_records(
Employee_ID INT PRIMARY KEY AUTO_INCREMENT,
Employee_Name VARCHAR(100) NOT NULL,
Email VARCHAR(100) NOT NULL,
Phone_Number VARCHAR(20) NOT NULL,
Department VARCHAR(100) NOT NULL,
Designation VARCHAR(100) NOT NULL,
Salary FLOAT NOT NULL,
Joining_Date DATE NOT NULL
);

INSERT INTO employee_records(Employee_Name, Email, Phone_Number, Department, Designation, Salary, Joining_Date) VALUES
("Varun", "varun@gmail.com", "9876543213", "Sales","Senior Salaes Executive", 23000, "2022-06-01"),
("Kavin", "kavin@gmail.com", "8901235436", "Accounts", "Junior Accountant", 25000, "2020-02-01"),
("Pavin", "pavin@gmail.com", "7890123456", "HR", "HR Manager", 35000, "2021-06-01"),
("Praveen", "praveen@gmail.com", "6789012345", "Management", "Assistant Manager",38000, "2023-03-06"),
("Surya", "surya@gmail.com", "6789654326", "Accounts", "Senior Accountant", 22000, "2020-09-15")
;

select * from employee_records;
