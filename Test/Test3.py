import os 

if os.path.isfile('data.txt'):
    print('File is exits')
else:
    print('File is not exits')