class Stack:

    def __init__(self, size):
        self.size = size
        self.top = -1
        self.a = [None for i in range(size)]

    def push(self, val):
        if self.top == self.size-1:
            print('Stak is full...')
        else:
            self.top += 1
            self.a[self.top] = val

    def pop(self):
        if self.top == -1:
            print('Stack is Empty ...')
        else:
            b = self.a[self.top]
            self.top -= 1
            return b
        return None

    def show(self):
        if self.top == -1:
            print('Stack is Empty ...')
        else:
            start=self.top
            while start >=0:
                print("|",self.a[start],"|")
                start-=1
    


s = Stack(10)
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(40)
s.push(40)
s.push(40)
s.push(40)
s.push(40)
s.push(40)
s.push(40)
s.push(40)
s.push(40)

s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.pop()
s.show()

s = Stack(3)

