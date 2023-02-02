import copy

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
    m = copy.deepcopy(m1)
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            m[i][j] = m1[i][j]+m2[i][j]
    return m


def subTwoMatrix(m1, m2):
    m = copy.deepcopy(m1)
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            m[i][j] = m1[i][j]-m2[i][j]
    return m

# 3*3 3*2 = 3*2
def mulTwoMatrix(m1, m2):
    c=[]
    for i in range(len(m1)):
        a=[]
        for j in range(len(m2[i])):
            a.append(0)
        c.append(a)

    if len(m1[0]) == len(m2):
        for i in range(len(m1)):
            for j in range(len(m2[i])):
                for k in range(len(m1[0])):
                    c[i][j]+=m1[i][k]*m2[k][j]
    else:
        print('Multiplication not possiable ....')
    return c


def printMatrix(m):
    for i in range(len(m)):
        print(m[i])


r = int(input(f'Enter Row 1 : '))
c = int(input(f'Enter Coloumn 1 : '))
m1 = MakeMatrix(r, c)

r = int(input(f'Enter Row 2 : '))
c = int(input(f'Enter Coloumn 2 : '))
m2 = MakeMatrix(r, c)

print('Perform Addition two Matrix :>')
printMatrix(addTwoMatrix(m1, m2))

print('Perform subtraction two Matrix :>')
printMatrix(subTwoMatrix(m1, m2))

print('Perform Multiplication two Matrix :>')
printMatrix(mulTwoMatrix(m1, m2))
