class Student:
    name = "Suvendu"
    clg = "MMCC"


def checkAttr():
    for k, v in Student.__dict__.items():
        if not k.startswith('_'):
            print(k, v)


print("Before delete Class Attribute : ")
checkAttr()

delattr(Student, 'name')

print("After delete Class Attribute : ")
checkAttr()
