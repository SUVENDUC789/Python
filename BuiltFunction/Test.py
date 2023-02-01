'''
● abs() 
'''
# print(abs(-108))
# a=[-1,-2,-3,-4,-5]
# b=[abs(i) for i in a]
# print(b)
'''
● bin() 
'''
# print(bin(10))
'''
● exec() 
'''
# exec('print(min(10,20))')
# exec('print(max(10,20))')
'''
● format() 
'''
# a='Hi i am {} {}'.format('Iron','Man')
# a='Hi i am {1} {0}'.format('Iron','Man')
# a='Hi i am {name1} {name0}'.format(name1='Iron',name0='Man')
# print(a)
'''
● getattr() 
'''
# class Friend:
#     name='Suvendu'
#     @staticmethod
#     def greet():
#         return "Hi sir how are you"
#     pass

# print(getattr(Friend,'name','sup'))
# print(getattr(Friend,'greet')())

'''
● setattr() 
'''
# setattr(Friend,'clg','MMCC')
# print(Friend.clg)
'''
● hasattr() 
'''
# attr='name'
# if hasattr(Friend,attr):
#     print(f"{attr} present in Friend class")
# else:
#     print(f"{attr} is not present in the Friend class")

'''
● iter() 
set , list , tuple , string are itterable object
so iter() function only take as a argument itterable
'''
# iter((1,2,3))
# a=[i for i in range(10)]
# a=iter(a)
# print(a)
# print(type(a))
# print(next(a))

'''
● map()
'''
# def power2(n):
#     return n**2

# a = [str(i) for i in range(1, 10, 2)]
# a = list(map(int, a))
# print(a)
# a = list(map(lambda x: x*x, a))
# print(a)

''' 
● objects() 
'''

'''
● open() 
● enumerate() ---> builtin python function return List items and index value
'''
# a = ['Avas', 'Bristi', 'Debu', 'Sup', 'Hri']
# a.sort(reverse=True)
# for k, v in enumerate(a):
#     print(k, v)

'''
● filter() 
'''
# def even(n):
#     return n % 2 == 0

# a = [i for i in range(1, 11)]

# # if function return truw then consider the value other wise not
# a = list(filter(even, a))
# print(a)

'''
● hash() ---> function return hash value
'''
# print(hash(1))
# print(hash(1.0))
# print(hash("{1,2,3}"))
# print(hash("{1,2,3}"))
'''
● slice() 
● next() 
'''


def s(a, b):
    '''<generator object s at 0x0000022637746440>
<class 'generator'>       
yield keyword in python create generate class object'''
    yield a
    yield b


# x, y = s(10, 20)
# print(s(10, 20))
# print(type(s(10, 20)))
# print(x, y)


# def ownRange(a, b):
#     while a <= b:
#         yield a
#         a += 1


# a = ownRange(5, 7)
# print(next(a))
# print(next(a))
# print(next(a))

# print(next(a))  # throw error

'''
● reversed() 
'''
# a=[i for i in range(10,20,2)]
# print("Before reverse : ",a)
# a.reverse()
# print("After reverse : ",a)

'''
● sorted() argument type is any itterable but return type is  sorted list
'''
# a=('Bristi','Hritik','Suvendu','Supratim','Avas','Debarpan')
# print(sorted(a))

'''
● round() 
this function return type is number
round(Number(Mandetary field),digit(Optianal))
'''
# print(round(2.333333456))
# print(round(2.5559999988888))
# print(round(2.5559999988888,  2))
'''
● type() 
'''
# print(type([i for i in range(10)]))
'''
● vars() 
● zip()
'''
