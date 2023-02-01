class Student:
    pass

def diolog():
    return "I am iron man"

setattr(Student,'name',"Suvendu Chowdhury")
print(getattr(Student,'name'))

setattr(Student,'dt',diolog)
print(getattr(Student,'dt')())