class Employee:
    def __init__(self, name, age, sem):
        self.name = name
        self.age = age
        self.sem = sem

    def details(self):
        print("Name : ", self.name,end="    ")
        print("Age : ", self.age,end="  ")
        print("Semester : ", self.sem)


# suv = Employee("Suvendu", 20, 5)
# debu = Employee("Debarpan", 20, 5)

# print(suv.__dict__)
# suv.name = "Suvendu"
# debu.name = "Debarpan"
# suv.details(), debu.details()
