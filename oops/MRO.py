# Method Resolution Order

class Father:
    def __init__(self):
        super().__init__()
        print("Father class constructor ")


class Mother:
    def __init__(self):
        # super().__init__()
        print("Mother class constructor ")


class Son(Father, Mother):
    '''******Like a Graph traversal******'''
    def __init__(self):
        super().__init__()
        print("Son class constructor ")


s = Son()

print(Son.__doc__)
