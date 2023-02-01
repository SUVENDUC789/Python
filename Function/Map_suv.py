power = lambda x,y=2: x**y 

a=[i for i in range(1,11)]

result = map(power,a)

for i in result:
    print(i)
    
print(result)
print(type(result))