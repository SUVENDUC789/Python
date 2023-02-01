class Queue:

    def __init__(self, size):
        self.size = size
        self.font = -1
        self.rear = -1
        self.a = [None for i in range(size)]

    def insert(self, val):
        if self.rear == self.size-1:
            print('Queue is full ...')
        else:
            self.rear += 1
            self.a[self.rear] = val

    def remove(self):
        if self.font == self.rear:
            print('Queue is empty ...')
        else:
            self.font += 1
            return self.a[self.font]
        return None

    def show(self):
        if self.font == self.rear:
            print('Queue is empty ...')
        else:
            for i in range(self.font+1, self.rear+1):
                print(self.a[i], end =' , ')


if __name__ == '__main__':
    q = Queue(10)
    q.insert(10)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(5)
    q.insert(20)

    q.show()

    q.remove()
    q.remove()
    q.remove()
    q.remove()
    q.remove()
    q.remove()
    q.remove()
    q.remove()
    q.remove()

    q.show()
