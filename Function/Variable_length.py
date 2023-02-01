def varArgsInC(*c):
    '''Variable length arguments its work like a touple'''
    print(type(c))
    print(c)


# print(varArgsInC.__doc__)
# varArgsInC(1, 2, 3, "Suvendu")


def varArgsInC2(**c):
    '''Variable length-2 arguments its work like a Dictionary '''
    print(type(c))
    print(c)


info = {
    "name": "Suvendu Chowdhury",
    "collage": "MMCC",
    "Department": "BSC",
    "Sem": 5,
    "Last sem Cgpa": 7.1
}

print(varArgsInC2.__doc__)
varArgsInC2()
