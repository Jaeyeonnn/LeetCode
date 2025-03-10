# Write your MySQL query statement below
SELECT 
    employee_id, 
    COALESCE(
        (SELECT department_id FROM Employee e2 WHERE e2.employee_id = e1.employee_id AND primary_flag = 'Y'),
        (SELECT department_id FROM Employee e2 WHERE e2.employee_id = e1.employee_id LIMIT 1)
    ) AS department_id
FROM 
    Employee e1
GROUP BY 
    employee_id;
