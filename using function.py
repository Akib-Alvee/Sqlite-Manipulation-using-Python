import sqlite3
from employee import Employee
import json

# conn = sqlite3.connect('employee.db')

# everytime create fresh table in RAM
conn =sqlite3.connect(':memory:')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE Employees(
                FirstName text,
                LastName text,
                Salary integer
                )""")


emp_1 = Employee('Akib','Alvee',50000)
emp_2 = Employee('Abdul','Babdul',60000)
emp_3 = Employee('Akib','Sakib',50000)
emp_4 = Employee('Fahimur','Rashid',60000)
emp_5 = Employee('Badrul','Mashfy',70000)
emp_6 = Employee('Omar','Faruqe',80000)
emp_7 = Employee('Fahim','Shah',90000),
emp_7 = Employee('Jahedul','Nowshad',100000)

def insertEmployee(emp):
    with conn:
        cursor.execute("INSERT INTO employees VALUES (:firstName, :lastName, :salary)", 
                       {'firstName': emp.firstName, 'lastName': emp.lastName, 'salary': emp.salary})

def getAllEmployee():
    cursor.execute("SELECT * FROM Employees")
    return cursor.fetchall()

def getEmployeeByFirstName(firstName):
    cursor.execute("SELECT * FROM employees WHERE firstName=:firstName", {'firstName': firstName})
    return cursor.fetchall()


def updateSalary(emp,salary):
    with conn:
        cursor.execute("""UPDATE employees SET salary = :salary
                    WHERE firstName = :firstName AND lastName = :lastName""",
                  {'firstName': emp.firstName, 'lastName': emp.lastName, 'salary': salary})


def removeEmployee(emp):
    with conn:
        cursor.execute("DELETE from employees WHERE firstName = :firstName AND lastName = :lastName",
                  {'firstName': emp.firstName, 'lastName': emp.lastName})
        

insertEmployee(emp_1)
insertEmployee(emp_2)
insertEmployee(emp_3)
insertEmployee(emp_4)
insertEmployee(emp_5)
insertEmployee(emp_6)
insertEmployee(emp_7)

emp= getAllEmployee()

print(emp)

emps = getEmployeeByFirstName ('Akib')
print(emps)

updateSalary(emp_2, 95000)
removeEmployee(emp_1)

print(getAllEmployee())

conn.commit()
conn.close()

with open('employee.json','w') as f:
    json.dump(emp,f,indent=2)