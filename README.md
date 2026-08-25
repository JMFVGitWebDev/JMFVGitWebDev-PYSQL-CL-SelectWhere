# Background

SQL sublanguage: DQL (Data Query Language)

Now that we know how to query all records from a table utilizing the "SELECT" keyword, it might be beneficial to
filter what records are given to us from a table using the WHERE keyword.

SELECT \* FROM employee WHERE first_name = 'Steve';

In addition to filtering on equality, we can filter on inequality with the `<`, `>`, `<=`, `>=`, and `!=`
operators. We can even filter on strings that match partially, using the `LIKE` keyword and the `%` wildcard.

## Problem 1

Assume the following table already exists.

| id  | first_name | last_name | salary    |
| --- | ---------- | --------- | --------- |
| 1   | Steve      | Garcia    | 67400.00  |
| 2   | Alexa      | Smith     | 42500.00  |
| 3   | Steve      | Jones     | 99890.99  |
| 4   | Brandon    | Smith     | 120000.00 |
| 5   | Adam       | Jones     | 55050.50  |
| 5   | Casey      | Bondary   | 75000.00  |

Write a query in `problem1.sql` to retrieve all the records from the `employee` table that have the last_name
'Smith'.

## Problem 2

Using the same table above, write a query in `problem2.sql` to retrieve all the records from the `employee`
table that have a salary greater than $75000.
