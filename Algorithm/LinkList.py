class Node:
    __data = 0
    Next = None

    def __init__(self, v):
        self.__data = v

    def getData(self):
        return self.__data
    


class LinkList:
    def traversal(head):
        while (head != None):
            print("|", head.getData(), "|")
            head = head.Next


head = Node(10)
n1 = Node(20)
n2 = Node(30)
last = Node(40)

# print(head.__data)
head.Next = n1
n1.Next = n2
n2.Next = last
last.Next = None

LinkList.traversal(head)
