class Duck:
    def walk(self):
        print("Duck : Thapak thapak thapak thapak")


class Hourse:
    def walk(self):
        print('Hourse : Takbak takbak takbak takbak')


class Cat:
    def talk(self):
        print('Cat : Meaow meaow')


def myfun(obj):
    '''With out use hasattr()-->it is like duck typing
    use hasattr()-->it is like Strong Typing

    it is use just for handeling error with out using Exception handeling'''

    if hasattr(obj, 'walk'):
        obj.walk()
    elif hasattr(obj, 'talk'):
        obj.talk()
    else:
        print('Attribute Error.')


if __name__ == '__main__':
    d = Duck()
    myfun(d)

    h = Hourse()
    myfun(h)

    # this throw error in duck typing and Strong Typing
    c = Cat()
    myfun(c)

    print(myfun.__doc__)  # Using Docstring
