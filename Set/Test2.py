'''
- Unordered
- Unindexed
- Itterable

set()  is mutable object .
add()
pop()
remove()
clear()
discard()
update()
intersection()
union()
'''

s = set()

# using add method
s.add(10)
s.add(20)
s.add(1)

s.update([9, 6, 7, 4])

print("Poped element is : ", s.pop())
s.remove(20)  # remove 20
s.remove(9)  # remove 20
# s.clear()  # set clear

print(s)


# union and intersection

a = set([10, 20, 30])
b = set([1, 2, 3, 30])

print("Intersection : ", a.intersection(b))
print("Union : ", a.union(b))
print("Difference : ", a.difference(b))
