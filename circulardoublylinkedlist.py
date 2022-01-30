class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next:
                break

    #Creation of Circular Doubly Linked List
    def createCDLL(self,nodeValue):
        newNode=Node(nodeValue)
        self.head=newNode
        self.tail=newNode
        newNode.prev=newNode
        newNode.next=newNode
        return "The Circular doubly linked list is created successfully."
    #Insertion of Circular Doubly Linked List
    def insertCDLL(self,value,location):
        if self.head is None:
            return "The Circular Doubly linked list does not exist."
        else:
            newNode=Node(value)
            if location==0:
                newNode.next=self.head
                newNode.prev=self.tail
                self.head.prev=newNode
                self.head=newNode
                self.tail.next=newNode
            elif location==1:
                newNode.next=self.head
                newNode.prev=self.tail
                self.head.prev=newNode
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while  index<location-1:
                    tempNode=tempNode.next
                    index +=1
                newNode.next=tempNode.next
                newNode.prev=tempNode
                newNode.next.prev=newNode
                tempNode.next=newNode
            return "The node has been successfully inserted."


CircularDLL=CircularDoublyLinkedList()
print(CircularDLL.createCDLL(5))
CircularDLL.insertCDLL(0,0)
CircularDLL.insertCDLL(1,1)
CircularDLL.insertCDLL(2,2)
CircularDLL.insertCDLL(3,3)
CircularDLL.insertCDLL(4,4)
print([node.value for node in CircularDLL])
