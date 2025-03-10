# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT num, 
           LEAD(num) OVER (ORDER BY id) AS next_num,
           LEAD(num, 2) OVER (ORDER BY id) AS next_num_2
    FROM Logs
) AS consecutive_nums
WHERE num = next_num AND num = next_num_2;
