class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        

    

    @property
    def name(self):
        return self._name
    @property
    def salary(self):   
        return self._salary 
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            self._salary = 0
            raise ValueError("El salario no puede ser negativo")
        else:
            self._salary = new_salary
    
    def promote(self, percentage_to_increase):
        return self._salary + self._salary * percentage_to_increase 
        

try:
    employee = Employee("Luis", 1000)
    employee.salary = employee.promote(0.1)
    print(employee.name)
    print(employee.salary)
except ValueError as ex:
    print(ex)



