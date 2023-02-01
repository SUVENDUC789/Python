
# Using String Format function
w = "Hello my name is {} {}.".format("Suvendu", "Chowdhury")
print(w)

w = "Hello my name is {1} {0}.".format("Suvendu", "Chowdhury")
print(w)

w = "Hello my name is {fname} {lname}.".format(
    fname="Suvendu", lname="Chowdhury")
print(w)

# Using Percentage Operator
p = "Roll %d | Marks %.1f | Name %s" % (412, 7.1, 'Suvendu Chowdhury')
print(p)

# This is called eaw string
rowString = r"My name is Suvendu \n And i am iron man"
print(rowString)


# f-strings
a = [1, 2, 3, 4]
for i in a:
    print(f'Output-{i}')
