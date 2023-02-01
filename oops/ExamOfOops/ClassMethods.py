# dry principle --> Do not repeat itself
class Student:
    noOfLeav = 10
    #  Constructor

    def __init__(self, name, roll, sem):
        self.name = name
        self.roll = roll
        self.sem = sem
        pass

    def details(self):
        print(f'Name : {self.name} Roll : {self.roll} Sem : {self.sem}')

    @classmethod
    def changeLeav(cls, n):
        cls.noOfLeav = n

    # Class Methods As Alternative Constructors
    @classmethod
    def setConstructor(cls, value):
        # params=value.split('-')
        # return cls(params[0],params[1],params[2])

        return cls(*value.split('-'))


# Class Methods As Alternative Constructors
bristi = Student.setConstructor('Bristi-416-5')
bristi.details()

swati = Student.setConstructor('Swati-420-5')
swati.details()

# create object
suv = Student('Suvendu', 412, 5)
# suv.noOfLeav = 20
suv.changeLeav(20)

print(suv.noOfLeav)

sup = Student('Supratim', 411, 5)
print(sup.noOfLeav)
