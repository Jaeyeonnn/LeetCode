# Write your MySQL query statement below


SELECT a.product_name, b.year, b.price FROM Sales b
LEFT JOIN Product a
on a.product_id = b.product_id 
