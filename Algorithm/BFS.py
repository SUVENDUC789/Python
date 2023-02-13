import copy

class ExplorationQueue:

    def __init__(self, size):
        self.size = size
        self.font = -1
        self.rear = -1
        self.a = [0 for i in range(size)]

    def isFull(self):
        if self.rear == self.size-1:
            return True
        return False

    def isEmpty(self):
        if self.font == self.rear:
            return True
        return False

    def enQueue(self, val):
        if self.rear == self.size-1:
            print('Queue is full ...')
        else:
            self.rear += 1
            self.a[self.rear] = val

    def deQueue(self):
        if self.font == self.rear:
            print('Queue is empty ...')
        else:
            self.font += 1
            return self.a[self.font]
        return None


if __name__ == '__main__':
    graph = [
        [0, 1, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1, 0, 0],
        [1, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0]
    ]
    # print(graph)

    q = ExplorationQueue(7)
    v=copy.deepcopy(q.a)
    # Marks all node is unvisited
    # print(q.a)

    # Mark source node is visited
    start = 0
    print(start,end=' ')
    v[start] = 1

    # Enque the source node
    q.enQueue(start)

    while q.isEmpty()!=True:
        u = q.deQueue()
        # print(u)
        for i in range(7):
            if graph[u][i] == 1 and v[i] == 0:
                print(i,end=' ')
                v[i] = 1
                q.enQueue(i)

    # print(v)
