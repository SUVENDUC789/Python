# Simple Encapsulation or Access modifier
class Car:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed
        
    # This is the private method in python 
    def __details(self):
        print(self.__name)
        print(self.__speed)


audi=Car("Audi",350)

audi._Car__details()

