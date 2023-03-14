#для вибору певних стовпців із employee таблиці та обчислення додаткових стовпців
SELECT 
    #об’єднуєм стовпці first_nameта last_name в один full_name стовпець
    CONCAT(first_name, ' ', last_name) AS full_name, 
    salary, 
    #обчислюєм 15% зарплати працівника як податок
    0.15*salary AS taxes, 
    #обчислюєм зарплату працівника після сплати податків
    (salary - 0.15*salary) AS net_salary, 
    #обчислюєм загальну зарплату всіх працівників у таблиці
    (SELECT SUM(salary) FROM employee) AS total_salary, 
    #обчислюєм мінімальну зарплату серед усіх працівників у таблиці
    MIN(salary) AS min_salary, 
    #обчислюєм максимальну зарплату серед усіх працівників у таблиці
    MAX(salary) AS max_salary, 
    #обчислюєм середню заробітну плату серед усіх працівників таблиці
    AVG(salary) AS average_salary, 
    #обчислюєм кількість працівників у таблиці
    COUNT(*) AS employee_count 
FROM employee 
#впорядковує результати за full_nameстовпцями в порядку зростання
ORDER BY full_name ASC;
