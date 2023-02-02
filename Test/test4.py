# Three way to file closing technique
#       1. use close state ment 
#       2. use exception handeling 
#       3. with statement 

# 1st way 
f=open('data.txt')
print('3 way to file closing technique ...')
f.close()

# 2nd way 
try:
    f=open('data.txt')
    print('3 way to file closing technique ...')
finally:
    f.close()
    
# 3rd way 
with open('data.txt') as f:
    print('3 way to file closing technique ...')
    # f.open('data.txt')
    