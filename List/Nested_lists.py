# The split and join methods
m = "Suvendu Chowdhury"
print(m.find('ow'))
print(m.count('u'))
m = m.split()
print(m)
m = ' '.join(m)
print(m)


# List comprehensions
a = [i for i in range(10) if i % 2 == 0]
print(a[:3])
b = [i for i in range(10) if i % 2]
a.extend(b)
print(a)


def NestedList():
    a = []
    for i in range(3):
        b = []
        for j in range(3):
            num = int(input(f"Enter number [{i}][{j}] : "))
            b.append(num)
        a.append(b)

    print("Nested list Exemple : ")
    for i in range(3):
        print(a[i])
