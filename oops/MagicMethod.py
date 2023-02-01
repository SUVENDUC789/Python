class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return self.salary+other.salary

    def __repr__(self):
        return f'<Employee ({self.name} , {self.salary})>'


suv = Employee("Ram", 10)
sup = Employee("Ram", 20)
print(str(suv))

# debu = sup+suv
# print(suv,debu)
