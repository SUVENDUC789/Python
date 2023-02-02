f=open('data.txt')
data=f.readlines()
print(data)
f.close()

f=open('data1.txt','a')
for i in data:
    f.write(i)
f.close()