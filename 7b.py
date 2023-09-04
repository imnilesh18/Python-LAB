class Employee:
    tot = 0

    def __init__(self, name, eid, dept, salary):
        self.name = name
        self.Employee_ID = eid
        self.Department = dept
        self.salary = salary
        Employee.tot += 1

    def update_salary(self, percent):
        self.salary = self.salary + (self.salary * percent / 100)

    def display(self):
        print("Name: ", self.name)
        print("ID: ", self.Employee_ID)
        print("Department: ", self.Department)
        print("Salary: ", self.salary)


emp = []
print("===============================================================")
n = int(input("Enter the number of Employees: "))

if n < 1:
    print("Invalid value of number of Employees, stopping execution...")
    exit()

for x in range(n):
    name = input("Enter the name of the Employee %d: " % (x+1))
    eid = input("Enter the ID of the Employee %d: " % (x + 1))
    dept = input("Enter the Department of the Employee %d: " % (x + 1))
    salary = int(input("Enter the Salary of the Employee %d: " % (x + 1)))

    emp.append(Employee(name, eid, dept, salary))
    print("\n")

print("===============================================================")
print("\n")

print("Below are the entered details of the employees: ")

print("===============================================================")
for x in range(n):
    emp[x].display()
    print("\n")
print("===============================================================")

dept = input("Enter the department of the employee: ")
hike = int(input("Enter the percentage of hike in the salary: "))
if hike > 100 or hike < 0:
    print("Invalid value of hike, stopping execution...")
    exit()
    print("===============================================================")

print("===============================================================")
print("Updating the salary of the employees...")
for x in range(n):
    if dept == emp[x].Department:
        emp[x].update_salary(hike)

print("Successfuly updated the salary of the employees")
print("===============================================================")

print("===============================================================")
print("Final employee details with updated salary: ")
for x in range(n):
    emp[x].display()
    print("\n")

# print("Total number of Employee objects created:", Employee.tot)
