class Length:
    def __init__(self,l=0):
        self.length = l

    def setLength(self,l):
        self.length = l
    
    def getLength(self):
        return self.length

    def __str__(self):
        return str(self.length)

    def __add__(self,obj):
        return self.length+obj.length


obj1=Length(10)
obj2=Length(20)
obj3=Length()

print('Length 1 is : ',obj1)
print('Length 2 is : ',obj2.getLength())

obj3.setLength(50)
print('Length 1 is : ',obj3)
print("Sum of two object : ",obj1+obj2)