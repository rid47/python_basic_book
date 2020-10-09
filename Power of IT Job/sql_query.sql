/*

Q: There was two table Student(Id, Name), Grade (Id, Subject, Mark)

a) Show the average marks of each student (There was a output table) like output table.
b) Find the name of all student who have got marks > 59

*/

/* for answering we used db test of localhost*/

SELECT student_id, AVG(Mark) FROM grade GROUP BY student_id

SELECT 
  grade.student_id,
  student.name 
FROM
  grade 
  LEFT JOIN student 
    ON student.`student_id` = grade.`student_id` 
WHERE grade.Mark > 59 
GROUP BY student_id


/* query

employee1(id, name, salary, join-date)
employee2(id, name, salary, join-date)

a. write a query which shows details of emplyee1 where name ends with m and
show in ascending order by name?
b. show id, name, salary, join-date of employee 1 and employee2 where salary
is greater than 660000 and order by salary desc

*/

SELECT * FROM employee1 WHERE NAME LIKE '%m' ORDER BY NAME ASC

/*
WHERE CustomerName LIKE 'a%'	Finds any values that start with "a"
WHERE CustomerName LIKE '%a'	Finds any values that end with "a"
WHERE CustomerName LIKE '%or%'	Finds any values that have "or" in any position
WHERE CustomerName LIKE '_r%'	Finds any values that have "r" in the second position
WHERE CustomerName LIKE 'a_%'	Finds any values that start with "a" and are at least 2 characters in length
WHERE CustomerName LIKE 'a__%'	Finds any values that start with "a" and are at least 3 characters in length
WHERE ContactName LIKE 'a%o'	Finds any values that start with "a" and ends with "o"
*/

SELECT `id`,`name`,`salary`, `join-date` FROM employee1 WHERE salary > 66000 
UNION
SELECT `id`,`name`,`salary`, `join-date` FROM employee2 WHERE salary > 66000 

ORDER BY salary DESC


/*

2 tables employee and department

a. find employee info from employee who had joined between date 21-Jan-2013 and 31 jan 2018
b. find employee id, name, avg salary who are in sales department shwo them in ascending order

*/

SELECT * FROM employee WHERE joining_date BETWEEN '2013-01-21' AND '2018-01-31'

SELECT 
    department.emp_id,
    employee.`Name`,
    AVG(employee.`salary`) AS avg_salary 
  FROM
    department 
 
    LEFT JOIN employee 
      ON employee.`emp_id` = department.`emp_id` 
      
       WHERE department.`dept_name` = 'sales' 