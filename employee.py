class Employee:
    
    def __init__(self,firstName,lastName,salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.firstName,self.lastName)
    
    
    @property
    def fullname(self):
        return '{}.{}'.format(self.firstName,self.lastName)
    
    
    @property
    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.firstName,self.lastName,self.salary)