# example of instance vairables 
class Employee: 
    raise_amount= 1.04
    num_of_employees= 2 

    def __init__(self, first, last, pay):
        self.first= first
        self.last= last 
        self.email= first+'.'+ last +'@company.com'
        self.pay= pay 

    def fullname(self):
        return('{}, {}'.format(self.first, self.last))
    def apply_raise(self):
        self.pay= int(self.pay*self.raise_amount)
    @classmethod
    # an example of using a class method for raise amount 
    def set_raise_amt(cls, amount):    
        cls.raise_amt= amount
    @classmethod
    def fromstring(cls, emp_str):
        first, last,pay = emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_work_day(day):
        if day.weekday() ==5 or  day.weekday() ==6 :
            return False
        return True
emp_1 = Employee('Rus', 'Smith',  50000 )
emp_2= Employee('Test', 'User', 60000)
emp_str_1= 'John-Doe-7000'
emp_str_2='Steve-Smith-3000'
emp_str_3='Jane-Doe-1000'
new_emp_1 = Employee.fromstring(emp_str_1)

emp_1.raise_amount=1.05
print(emp_1.__dict__)
emp_1.fullname()
Employee.set_raise_amt(1.05)
print(Employee.fullname(emp_1))

print("The number of Employee is: ",Employee.num_of_employees)

print("The Employee Raise Amount is: ", Employee.raise_amt )
print("The Raise Amount for Employee1 is: ", emp_1.raise_amt)
print("The new employee  is: ", new_emp_1)

import datetime
my_date= datetime.date(2016, 7, 11)
print(Employee.is_work_day(my_date))

class Developer(Employee):
    raise_amt=1.10
    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        self.programming_language= programming_language
class Manager(Employee):
    pass
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if(employees is None):
            self.employees = []
        else:
            self.employees = employees 
    def add_employee(self, employee): 
        if employee  not  in self.employees: 
            self.employees.append(employee)
    def remove_employee(self, employee): 
        if employee  not  in self.employees: 
            self.employees.remove(employee)        
    def print_employees(self): 
         for employee in self.employees:
             print('--> ', employee.fullname())   


developer1= Developer('Rus','Smith', 5000, 'Python')
developer2= Developer('Test','User', 6000, 'C#' )
#print(developer1.pay)
print(developer1.programming_language)
Manager1= Manager('Andrew', 'Smith', 90000,[developer1])
print(Manager1.email)
Manager1.add_employee(developer2)
Manager1.print_employees()
print(issubclass( Developer, Employee))