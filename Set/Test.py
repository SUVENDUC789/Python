'''
- Unordered
- Unindexed
- Itterable
'''
s1 = set()

# set datatype in python do not contained duplicate value

s1.add(1)  # Add method in set
s1.add(2)
s1.add(3)
# print(s1[0])  # throw error


# s=set()
# print(type(s))


s = set([1, 2, 3, 4, 9, 6, 7, 4])
print(s.pop())
s.remove(9)
print(s)
s.discard(6)
s.clear()
print(s)


print("Intersection : ", s.intersection(s1))
print("Union : ", s.union(s1))
