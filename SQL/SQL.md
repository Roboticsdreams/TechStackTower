# SQL

[Tech-Interviews](../../README.md) -> [KnowledgeBase](../KnowledgeBase.md) -> [SQL](../SQL/SQL.md)

Interview questions for Data Analyst 2024.

1. How would you retrieve the second highest salary from a table called Employees without using LIMIT or TOP?
2. Write a query to display employees who joined in the same month but in different years from the Employees table.
3. Given two tables, Orders and Customers, write a query to find all customers who placed more than five orders in the last year.
4. How would you update the Department column in the Employees table based on a matching EmployeeID in another table called Departments?
5. Write a SQL query to find the total sales for each product category, but exclude categories with total sales less than a specific threshold (e.g., $10,000).
6. How would you create a Python function that reads a large CSV file in chunks and processes each chunk for data cleaning?
7. Write a Python script that takes a list of employee records, filters out records where the salary is below a certain value, and writes the filtered records to a new file.
8. How would you handle missing values in a dataset using pandas, and how would you decide which method to use (e.g., mean imputation vs. forward fill)?
9. Given a list of numbers, write a Python program to group the numbers into ranges (e.g., 1-10, 11-20) and count the number of elements in each range.
10. How would you connect to an SQL database using Python and fetch data into a pandas DataFrame for analysis?
11. How would you use VLOOKUP or INDEX-MATCH to find a value in one Excel sheet and return corresponding information from another sheet?
12. Write an Excel formula that calculates the weighted average of a set of numbers, where the weights are stored in another column.
13. How would you create a dynamic Excel dashboard that allows users to filter data by multiple criteria and display the results visually (e.g., via charts or pivot tables)?
14. Explain how you would use Excel Solver to optimize a product mix for maximizing profit under given constraints.
15. How can you create a measure that calculates the running total of sales over time, and how would you display it in a line chart?
16. How would you use Power Query to clean and transform a dataset, such as removing duplicates, splitting columns, and filtering rows based on conditions?
17. Describe a scenario where you would need to use Merge Queries in Power Query, and how would you do it?
18. How can you create a custom tooltip in Power BI to show additional information when a user hovers over a visual?

What is the difference between UNION and UNION ALL?
   • UNION: Removes duplicate rows
   • UNION ALL: Keeps all rows, including duplicates
   • UNION ALL is typically faster due to less processing

2. Explain the types of JOIN in SQL:
   • INNER JOIN: Returns matching rows from both tables
   • LEFT JOIN: All rows from left table, matching from right
   • RIGHT JOIN: All rows from right table, matching from left
   • FULL OUTER JOIN: All rows when there's a match in either table

3. What's the difference between WHERE and HAVING clauses?
   • WHERE: Filters individual rows before aggregation
   • HAVING: Filters groups after aggregation
   • Example: WHERE is used with SELECT; HAVING with GROUP BY

4. How do you optimize a slow SQL query?
   • Use EXPLAIN to analyze query execution plan
   • Add appropriate indexes
   • Avoid using SELECT *
   • Use JOINs instead of subqueries where possible

5. What is a self-join and when would you use it?
   • A table joined with itself
   • Useful for hierarchical data or comparing rows within a table