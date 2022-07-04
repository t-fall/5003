class Node:
    def __init__(self, dataval = None):
        self.data = dataval
        self.next = None
        self.prev = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next

    def AtBeginning(self,newdata):
            NewNode = Node(newdata)

    def AtEnd(self, newNode):
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while(last.next):
            last = last.next
        last.nexts = newNode

list = SLinkedList()
list.head = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Thur")
e5 = Node("Fri")
e6 = Node("Sat")
e7 = Node("Sun")

list.head.next = e2
e2.next = e3
e3.next = e4
e3.prev = e2
e4.next = e5
e4.prev = e3
e5.next = e6
e5.prev = e4
e6.prev = e5
e6.next = e7 #assigning the extra values added to the linked list
e7.prev = e6
list.AtEnd(e7)

list.listprint()
