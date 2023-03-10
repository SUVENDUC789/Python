# import thread class 

# create a function some executable code 

# create a new thread here 

# start the new thread 

from threading import Thread

def test2():
    for i in range(5):
        print(i,"Hello Pc")

def test():
    for i in range(5):
        print(i,"Hello World")


t1=Thread(target=test2)
t1.start()

t2=Thread(target=test)
t2.start()
