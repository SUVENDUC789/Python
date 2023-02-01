# dry principle --> Do not repeat itself
class Student:
    #  Constructor 
    def __init__(self, name, roll, sem):
        self.name = name
        self.roll = roll
        self.sem = sem
        pass

    def details(self):
        print(f'Name : {self.name} Roll : {self.roll} Sem : {self.sem}')


# create object
suv = Student('Suvendu',412,5)

# create instace variable
suv.name = "Suvendu Chowdhury"
# suv.age = 20

suv.details()
