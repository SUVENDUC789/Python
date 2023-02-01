class Student:
    name='suvendu'
    roll=412

    @staticmethod
    def diolog():
        return "I am iron man"

print(Student.name)
print(getattr(Student,'nameS',"supratim"))

print(Student.diolog())
print(getattr(Student,'diolog')())