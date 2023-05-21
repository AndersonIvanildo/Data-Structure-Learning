# Single Linked List Class
from Node_Class import Node # Import Node class from Node_Class.py

class SingleLinkedList: # class responsible for Single Linked List (SLL)
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.nextNode

    def traverseSLL(self): # Print all nodes values from SLL
        node = self.head
        while node:
            print(node.value)
            node = node.nextNode
        
    def insertNode(self, newNode=Node(None), location=-1):
        # newNode = Node(value) # Creation of a node with the new value to be inserted in the SLL

        if self.head == None: # If there is no node in the SSL
            self.head = newNode
            self.tail = newNode
        
        else: # Insert newNode at the specified position
            if location == 0: # Insert the node at the beginning of the list
                newNode.nextNode = self.head # The former first element becomes the nextNode of newNode
                self.head = newNode # newNode becomes the first node in SLL

            elif location == -1: # # Insert the node at the last position of the list
                newNode.next = None
                self.tail.nextNode = newNode # The last node of SLL now has as nextNode the node newNode
                self.tail = newNode # newNode now is the tail on SLL

            else: # Insert the node at specified location
                tempNode = self.head # node created to traverse the entire SSL to the specified location
                index = 0 # variable create to help in process

                while index < location - 1: # The tempNode will traverse SLL to the node before the desired location
                    tempNode = tempNode.nextNode
                    index += 1
                newNode.nextNode = tempNode.nextNode
                tempNode.nextNode = newNode

                if tempNode == self.tail: # If the tempNode is the last node of SLL
                    self.tail = newNode
        return True

    def searchNode(self, nodeValue): # Search for a node in SLL
        if self.head is not None: # If there is no node in the SSL
            node = self.head
            index = 0
            while node is not None: # Traverse the entire SLL
                if node.value == nodeValue:
                    return (node, index) # If the node is found
                node = node.nextNode
                index += 1
        return (None, -1) # If the node is not found
    
    def deleteNode(self, location): # Delete a node from SLL
        if self.head is None: # If there is no node in the SSL
            print("The list does not exist")
        else:
            if location == 0:
                if self.head == self.tail: # If there is only one node in the SLL
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.nextNode
            
            elif location == -1: # Delete the last node of the SLL
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else: # Traverse the entire SLL to find the node before the last node
                    node = self.head
                    while node is not None:
                        if node.nextNode == self.tail:
                            break
                        node = node.nextNode # The node before the last node
                    node.nextNode = None # The node before the last node now has no nextNode
                    self.tail = node # The node before the last node now is the last node
            else: # Delete the node at specified location
                tempNode = self.head
                index = 0
                while index < location - 1: # Traverse the entire SLL to find the node before the specified location
                    tempNode = tempNode.nextNode
                    index += 1
                nodeAfter = tempNode.nextNode # The node after the specified location
                tempNode.nextNode = nodeAfter.nextNode # The node before the specified location now has as nextNode the node after the specified location

    def deleteEntireSLL(self): # Delete the entire SLL
        self.head = None
        self.tail = None
