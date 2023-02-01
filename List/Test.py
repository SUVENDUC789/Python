'''List is mutable datatype in python you can change value in list'''

a = ['a', 'b', 'd']
a.sort(reverse=True)
print(a)

'''It does't change original list'''
a = [9, 6, 7, 4, 2, 8, 9, 2, 2, 0]
print(a[:3])
print(a[2:4])
print(a[:])


'''Builtin list method'''
a.append(108)  # (add new value in last of the list)
a.insert(2, 216)
a.remove(9)
a.pop()
print(a)


'''advanced slicing'''
print(a[::-1])
print(a[1:len(a):2])
print(a[-2])


'''some built in function '''
print("min : ",min(a))
print("max : ",max(a))

'''Conversion of list to tuple,set'''
print("List to set : ", set(a))
print("List to tuple : ", tuple(a))


'''Modifiaction in a will not effect in b vice versa'''
'''using copy method'''

a = [1, 2, 3, 4]
b = a.copy()
a[0] = 108
print(a)
print(b)

'''using List clone technique'''

a = [1, 2, 3, 4]
b = a[:]
a[0] = 108
print(a)
print(b)


'''but simple assignment list one to another'''
a = [1, 2, 3, 4]
b = a
a[0] = 108
print(a)
print(b)

'''index()'''

print(a.index(0))
print(a)

'''extend()'''

a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)
print(b)
