class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next==self.head:
                break
            node=node.next

    #Creation of circular singly linked list
    def  CreateCSLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return "The Circular Singly Linked linked list has been Created."

CircularSLL=CircularLinkedList()
CircularSLL.CreateCSLL(1)


print([node.value for node in CircularSLL])