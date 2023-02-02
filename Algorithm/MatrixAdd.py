def MakeMatrix(r, c):
    a = []
    for i in range(r):
        b = []
        for j in range(c):
            n = int(input(f'Enter number [{i}][{j}] : '))
            b.append(n)
        a.append(b)
    return a


def addTwoMatrix(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            m1[i][j] = m1[i][j]+m2[i][j]
    return m1


def printMatrix(m):
    for i in range(len(m)):
        print(m[i])


r = int(input(f'Enter Row 1 : '))
c = int(input(f'Enter Coloumn 1 : '))
m1 = MakeMatrix(r, c)

r = int(input(f'Enter Row 2 : '))
c = int(input(f'Enter Coloumn 2 : '))
m2 = MakeMatrix(r, c)

printMatrix(addTwoMatrix(m1, m2))
