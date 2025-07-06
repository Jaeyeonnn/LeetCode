# Write your MySQL query statement below
SELECT e.name as Employee 
FROM Employee as e
JOIN Employee as f
ON e.managerId=f.id
WHERE e.salary > f.salary

ORDER BY Employee