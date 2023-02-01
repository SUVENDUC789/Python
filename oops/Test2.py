import Test as t

a=[]
for i in range(3):
    name=input("Enter name : ")
    age=int(input("Enter age : "))
    sem=int(input("Enter sem : "))
    suv = t.Employee(name, age, sem)
    a.append(suv)

for i in range(3):
    a[i].details()

