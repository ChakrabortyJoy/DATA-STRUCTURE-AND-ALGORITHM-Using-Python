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
            node=node.next
            if node==self.tail.next:
                break

    #Creation of circular singly linked list
    def  CreateCSLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return "The Circular Singly Linked linked list has been Created."

    #Insertion of circular singly linked list
    def insertCSLL(self,value,location):
        if self.head is None:
            return "The head reference is None."
        else:
            newNode=Node(value)
            if location==0:
                newNode.next=self.head
                self.head=newNode
                self.tail.next=newNode
            elif location==1:
                newNode.next=self.tail.next
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been successfully inserted."
    
    #Traversal of a node in circular singly linked list
    def traversalCSLL(self):
        if self.head is None:
            print("There is not any element for Traversal")
        else:
            tempNode=self.head
            while tempNode:
                print(tempNode.value)
                tempNode=tempNode.next
                if tempNode==self.tail.next:
                    break

    #Seacrching of a node in circular single linked list
    def searchingCSLL(self,nodeValue):
        if self.head is None:
            return "There is not any node in this Circular singly linked list."
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value==nodeValue:
                    return tempNode.value
                tempNode=tempNode.next
                if tempNode==self.tail.next:
                    return "The node does not exist in this Circular singly linked list."

    # Delete a node from circular singly linked list
    def deleteNode(self,location):
        if self.head is None:
            print("There is not any node in Circular singly linked list.")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            elif  location==1:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    node=self.head
                    while  node is not None:
                        if node.next==self.tail:
                            break
                        node=node.next
                    node.next=self.head
                    self.tail=node
            else:
                tempNode=self.head
                index=0
                while  index<location-1:
                    tempNode=tempNode.next
                    index += 1
                newNode=tempNode.next
                tempNode.next=newNode.next

    # Delete entire circular sinlgy linked list
    def deleteEntireCSLL(self):
        self.head=None
        self.tail.next=None
        self.tail=None

CircularSLL=CircularLinkedList()
print(CircularSLL.CreateCSLL(0))
CircularSLL.insertCSLL(0,0)
CircularSLL.insertCSLL(2,1)
CircularSLL.insertCSLL(3,1)
CircularSLL.insertCSLL(2,2)

CircularSLL.traversalCSLL()

print(CircularSLL.searchingCSLL(4))

print([node.value for node in CircularSLL])

CircularSLL.deleteNode(0)

print([node.value for node in CircularSLL])

CircularSLL.deleteEntireCSLL()

print([node.value for node in CircularSLL])
