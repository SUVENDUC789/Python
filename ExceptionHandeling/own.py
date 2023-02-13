class Error(Exception):
    pass

class PornException(Error):        
        pass

print(str('hi').islower())
age =int(input('Enter your age : '))
try:
    if age >= 125:
        print('You also see porn')
    else:
        raise PornException
except PornException as e:
    print('You do not see porn but (Suvendu all time see Porn)')

finally:
    print('Programme noramlly terminated...')


