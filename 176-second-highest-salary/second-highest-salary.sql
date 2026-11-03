# Write your MySQL query statement below
select max(salary) as SecondHighestSalary from(select salary, dense_rank() over(order by salary desc)as t1 from Employee)t2 where t1=2; 