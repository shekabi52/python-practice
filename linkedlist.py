class Node:
    next = None
    data = 0

    def __init__(self, data):
        self.next = None
        self.data = data


class linkedlist:
    head = None

    def __init__(self):
        self.head = None

    def add(self, data):
        n = Node(data)
        if (self.head == None):
            self.head=n
        else:
            ite = self.head
            while (ite.next != None):
                ite = ite.next
            ite.next = n
        print(data,"added")

    def display(self):
        print("inside print")
        ite = self.head
        while (ite != None):
            print(ite.data, end="->")
            ite = ite.next


l = linkedlist()
l.add(10)
l.add(20)
l.add(30)
l.add(40)
l.display()