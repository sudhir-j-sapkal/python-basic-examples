class Employee:
    __id=0
    __name=""
    __gender=""
    __city=""
    __salary=0
    __dept_id=0

    def setEmployeeData(self):
        self.__id = int(input("Enter Id:\t"))
        self.__name = input("Enter Name:\t")
        self.__gender = input("Enter Gender:\t")
        self.__city = input("Enter City:\t")
        self.__salary = int(input("Enter Salary:\t"))
        self.__dept_id = int(input("Enter Department Id:\t"))
    
    def showEmployeeData(self):
        print("Id\t\t:",self.__id)
        print("Name\t:", self.__name)
        print("Gender\t:", self.__gender)
        print("City\t:", self.__city)
        print("Salary\t:", self.__salary)
        print("Department I\t:",self.__dept_id)
        

employees = list(());
#print(employees)
print("Enter Employee Details")
for i in range(1):
    #print(i);
    employee=Employee()
    employee.setEmployeeData()
    employees.append(employee)

for employee in employees:
    employee.showEmployeeData();

class Department:
    __id=0
    __name=""
    __emp_count=0

    def setDepartmentData(self):
        self.__id = int(input("Enter Id:\t"))
        self.__name = input("Enter Name:\t")
        self.__emp_count = int(input("Enter Employee Count:\t"))
        
    def showDepartmentData(self):
        print("Id\t\t:",self.__id)
        print("Name\t\t:", self.__name)
        print("Employee Count\t:",self.__emp_count)

departments = list(());
#print(employees)
print("\n\n Enter Department Details\n")
for i in range(1):
    #print(i);
    department=Department()
    department.setDepartmentData()
    departments.append(department)

for department in departments:
    department.showDepartmentData();

