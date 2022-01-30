class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    
    def traverseSLL(self):
        if self.head is None:
            print("The Singly Linked list does not exist")
        else:
            Node=self.head
            while Node is not None:
                print(Node.value)
                Node=Node.next
    
    def searchSLL(self,nodeValue):
        if self.head is None:
            return "The list does not exist"
        else:
            Node=self.head
            while Node is not None:
                if Node.value==nodeValue:
                    return Node.value
                Node=Node.next
            return "The value does not exist in this list"

singlyLinkedList=SLinkedList()
singlyLinkedList.insertSLL(1,1)
singlyLinkedList.insertSLL(2,1)
singlyLinkedList.insertSLL(3,1)
singlyLinkedList.insertSLL(4,1)

singlyLinkedList.insertSLL(0,0)
print([Node.value for Node in singlyLinkedList])
print(singlyLinkedList.searchSLL(3))