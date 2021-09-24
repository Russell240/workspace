class Employee:

    def __init__(self, first, last,job_postion, contract_type):
        self.first = first
        self.last = last
        self.job_postion= job_postion
        self.contract_type = contract_type
    @property    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)   
    @property
    def email(self): 
        return'{}{}@email.com' .format(self.first, self.last)            
    @fullname.setter
    def fullname(self, name): 
        first, last = name.split(' ')
        self.first= first
        self.last= last
     
    @fullname.deleter
    def fullname(self): 
         print("Delete this name !", ) 
         self.first = None
         self.last= None  
    @property    
    def jobpostion(self) :  
        return'{}{} is a {}'.__format__(self.first, self.last, self.job_postion)
    @property 
    def contracttype(self) : 
        return'{} {} is a {} employee'.format(self.first, self.last, self.contract_type)    

emp_1 = Employee('John', 'Smith','Admin','Part Time')
emp_1.fullname = "Corey Schafer"
emp_2 = Employee('Lee', 'Smith', 'Developer','Full Time')
emp_1.fullname="Lee Smith"
print(emp_1.first)
print(emp_1.email)
print(emp_1.job_postion)
print( "{0} is a {1} employee and works as a {2} ".format(emp_1.fullname, emp_1.contract_type, emp_1.job_postion))
print(emp_2.contract_type)
del emp_1.fullname