f=open('data.txt')

print(f.tell())
print(f.read(3))

f.seek(0)

print(f.tell())
print(f.read(3))