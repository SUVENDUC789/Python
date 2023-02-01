a = [i for i in range(10+10) if i % 2 == 0]
b = [i for i in range(10) if i % 2]

for i, j in zip(a, b):
    print(i, j)
