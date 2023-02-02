class Stack:
    def _init_(self,size):
        self.size = size
        self.top = -1
        self.a = [None for i in range(size)]
    
    def isEmpty(self):
        if self.top == -1:
            print('Stack is Empty ...')
        else:
            print('Stack is not empty...')


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
    
    def peek(self,num):
        if self.top == -1:
            print('Stack is Empty ...')
        else:
            try:
                print('Element are : ',self.a[num])
            except:
                print('Please eneter correct number ...')
            

    def show(self):
        if self.top == -1:
            print('Stack is Empty ...')
        else:
            start=self.top
            while start >=0:
                print("|",self.a[start],"|")
                start-=1

