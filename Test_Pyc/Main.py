class A:
    def show(self):
        print('Welcome')

    def show(self, name=''):
        print('Welcome : ', name)

    def show(self, name='', last=''):
        print('Welcome : ', name, last)

obj=A()
obj.show()
obj.show('Suvendu')
obj.show('Suvendu','Chowdhury')
