import sqlite3

conn = sqlite3.connect('employee.db')

# everytime create fresh table in RAM
# conn =sqlite3.connect(':memory:')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE Employees(
                FirstName text,
                LastName text,
                Salary integer
                )""")

cursor.execute("""INSERT INTO Employees (FirstName,LastName,Salary)
               VALUES
               ('Akib','Alvee',50000),
               ('Fahimur','Rashid',60000),
               ('Badrul','Mashfy',70000),
               ('Omar','Faruqe',80000),
               ('Fahim','Shah',90000),
               ('Jahedul','Nowshad',100000)
               """)

cursor.execute("SELECT * from Employees")

print(cursor.fetchall())

conn.commit()
conn.close()