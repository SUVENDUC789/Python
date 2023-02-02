try:
    f=open('data1.txt','a')
    if f:
        print('File opened successfully...')
    print(type(f))
    f.write('20')
except FileNotFoundError as e :
    print(e)