import sqlite3
from employee import Employee

# conn = sqlite3.connect('employee.db')

# everytime create fresh table in RAM
conn =sqlite3.connect(':memory:')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE Employees(
                FirstName text,
                LastName text,
                Salary integer
                )""")

# cursor.execute("""INSERT INTO Employees (FirstName,LastName,Salary)
#                VALUES
#                ('Akib','Alvee',50000),
#                ('Fahimur','Rashid',60000),
#                ('Badrul','Mashfy',70000),
#                ('Omar','Faruqe',80000),
#                ('Fahim','Shah',90000),
#                ('Jahedul','Nowshad',100000)
#                """)

emp_1 = Employee('Akib','Alvee',50000)
emp_2 = Employee('Abdul','Babdul',60000)
emp_3 = Employee('Akib','Sakib',50000)
emp_4 = Employee('Fahimur','Rashid',60000)
emp_5 = Employee('Badrul','Mashfy',70000)
emp_6 = Employee('Omar','Faruqe',80000)
emp_7 = Employee('Fahim','Shah',90000),
emp_7 = Employee('Jahedul','Nowshad',100000)

# one conventional method :::

# cursor.execute("INSERT INTO Employees VALUES (:firstName,:lastName,:salary)",
#                {'firstName':emp_1.firstName,'lastName':emp_1.lastName,'salary':emp_1.salary})
# conn.commit()

# another conventional method::::
# cursor.execute("INSERT INTO Employees VALUES (?,?,?)",(emp_2.firstName,emp_2.lastName,emp_2.salary))
# conn.commit()

cursor.execute("SELECT * from Employees")

print(cursor.fetchall())

conn.commit()
conn.close()