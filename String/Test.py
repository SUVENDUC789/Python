
s = "Hi i am rahul"

# print(s[1:7])# String slicing
# print(s[:7])
# print(s[:])
# print(s[5:])
# print(s[::-1])  # String reverse technique
# print(s[-1:-6:-1])  # String reverse technique

'''
● len() 
'''
print(len(s))

'''
● strip() 
● lstrip(),rstrip() 
'''
a = '!!!!!!!hello!!!!!!!!'
print(a.strip('!'))  # skip any character
a='aaaaaaaaaahelloaaaaaaaaaahelloaaaaaaaaaa'
print(a.strip('a'))

print(a.lstrip('a'))
print(a.rstrip('a'))

'''
● lower(),upper() 

'''
print(s.lower())
print(s.upper())

'''
● replace() 
'''
print(s.replace('am', 'are'))
'''
● split() 
'''
print(s.split(' '))  # split method return type is list
'''
● In ,not in keyword 
'''
print('rahul' in s)
print('rahul' not in s)
'''
● format() 
'''
a = "I am a {} {}".format('Iron', 'man')
a = "I am a {1} {0}".format('Iron', 'man')
a = "I am a {fname} {lname}".format(fname='Iron', lname='man')
print(a)
'''
● join() 
'''
s = s.split(' ')  # convert string to list
s = '@$%^'.join(s)  # convert list to string
print(s)

'''
● count() 
'''
b = 'Sexy Fuck sex hot AvaAddam Pornhut xhamstart.desi'
print(b.count('s'))  # return integer
'''
● casefold() 
'''
a='Hi BaBy HOw aRe U (TERI MAKI CHUD)'
print(a.casefold())
print(a.center(100))
'''
● capitalize()
'''
x = 'hi bro How aRe YoU i aM fiNe'
print(x.capitalize())

''' 
● find() 
'''

a = "Hello world how are you ?"
print(a.find('He'))  # return starting index
print(a.find('ho'))  # return starting index

'''
● isalnum() 
'''
print(a.isalnum())
'''
● inalpha() 
'''
# print(a.inalpha)
'''
● isnumeric() 
'''
a='9830thakthak48900fuckfuckAmer'
print(a.isnumeric())
'''
● isspace()
'''
a = '        '
print(a.isspace())
