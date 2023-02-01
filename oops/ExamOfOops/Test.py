# dry principle --> Do not repeat itself
class Student:
    phone = 8697757110
    pass


# create object
suv = Student()

# create instace variable
suv.name = "Suvendu Chowdhury"
suv.lang = ['Java', 'Dip']

print(suv.__dict__)
suv.phone = 9674289220
print(suv.__dict__)
print(type(suv.__dict__))

# print(Student.__dict__)

# print(suv.name, suv.lang)
