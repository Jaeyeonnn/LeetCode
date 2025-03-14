# Write your MySQL query statement below
SELECT s.user_id , round(ifnull(c2.confirm / c1.total,0),2)
         AS confirmation_rate
FROM signups s 
    left join (select user_id, count(*) as total from confirmations group by 1) c1 
    on s.user_id = c1.user_id
    left join (select user_id, count(*) as confirm from confirmations where action = 'confirmed' group by 1) c2 
    on s.user_id = c2.user_id ;