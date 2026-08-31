class Employee:
    def __init__(self, name, salary):
        
        if salary < 0:
            raise ValueError("El salario no puede ser negativo")
        self._name = name
        self._salary = salary
        # self.salary = self._salary
    

    @property
    def name(self):
        return self._name
    @property
    def salary(self):   
        return self._salary 
    @salary.setter
    def salary(self):
        return self._salary
    
    def promote(self, percentage_to_increase):
        self._salary += self._salary * percentage_to_increase 

try:
    employee = Employee("Luis", 1000)
    employee.promote(0.1)
    print(employee.name)
    print(employee.salary)
except ValueError as ex:
    print(ex)



