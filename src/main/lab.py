import os
import sqlite3

from src.main.user import User

"""
SQL sublanguage: DQL (Data Query Language)

Now that we know how to query all records from a table utilizing the "SELECT" keyword, it might be beneficial to
filter what records are given to us from a table.

For example lets look at the "employee" table below:
     employee table
     |  id  |   first_name   |   last_name   |  salary  |
     ----------------------------------------------------
     |1     |'Steve'         |'Garcia'       |67400.00  |
     |2     |'Alexa'         |'Smith'        |42500.00  |
     |3     |'Steve'         |'Jones'        |99890.99  |
     |4     |'Brandon'       |'Smith'        |120000.00 |
     |5     |'Adam'          |'Jones'        |55050.50  |
     |6     |'Casey'         |'Boundary'     |75000.00  |

Let's say we wanted to query all the records from the table that have the first name "Steve".

The statement that will be utilized is as follows:
SELECT * FROM employee WHERE first_name = 'Steve';

In addition to filtering on equality like above, we can filter on inequality with the <, >, <=, >=, and != operators.
We can even filter on strings that match partially, using the LIKE keyword and the '%' wildcard.
"""

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()



def _seeded_connection():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE employee(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        salary DOUBLE PRECISION
    );
    """)
    cur.execute("INSERT INTO employee (first_name, last_name, salary) VALUES ('Steve', 'Garcia', 67400.00);")
    cur.execute("INSERT INTO employee (first_name, last_name, salary) VALUES ('Alexa', 'Smith', 42500.00);")
    cur.execute("INSERT INTO employee (first_name, last_name, salary) VALUES ('Steve', 'Jones', 99890.99);")
    cur.execute("INSERT INTO employee (first_name, last_name, salary) VALUES ('Brandon', 'Smith', 120000.00);")
    cur.execute("INSERT INTO employee (first_name, last_name, salary) VALUES ('Adam', 'Jones', 55050.50);")
    cur.execute("INSERT INTO employee (first_name, last_name, salary) VALUES ('Casey', 'Boundary', 75000.00);")
    conn.commit()
    return conn, cur


def problem1():
    """
    Problem 1: Given the employee table, write a query in the problem1.sql file to retrieve all the records
    from the employee table that have the last_name 'Smith'

    NOTE: Please write the SQL statement on a single line (do not use multi-line formatting).
    """
    sql = _read_sql("problem1.sql")

    conn, cur = _seeded_connection()

    users = []
    try:
        cur.execute(sql)
        for row in cur.fetchall():
            users.append(User(row[0], row[1], row[2], row[3]))
    except Exception as e:
        print(f"problem1: {e}\n")
    finally:
        conn.close()

    return users


def problem2():
    """
    Problem 2: Given the employee table, write a query in the problem2.sql file to retrieve all the records
    from the employee table that have a salary greater than $75000

    NOTE: Please write the SQL statement on a single line (do not use multi-line formatting).
    """
    sql = _read_sql("problem2.sql")

    conn, cur = _seeded_connection()

    users = []
    try:
        cur.execute(sql)
        for row in cur.fetchall():
            users.append(User(row[0], row[1], row[2], row[3]))
    except Exception as e:
        print(f"problem2: {e}\n")
    finally:
        conn.close()

    return users
