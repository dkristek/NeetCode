#problem asks to desing either a singly or doubly linked list
#this is my solution for a doubly linked list
#problem: https://leetcode.com/problems/design-linked-list/
class Node:
    #node to use in lists. Val stores the value
    #next points to the next node in the list
    #prev points to the preceding node in the list
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    #creates a doubly linked list
    #has get, add at tail, add at head, add at index, 
    #and delete at index functions
    
    def __init__(self):
        self.size = 0
        self.head = None #first node of list
        self.tail = None #last node of list
        
    #will return the value of the node at the given index
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        if index < self.size// 2:
            curr = self.head
            for i in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for i in range(self.size -1, index, -1):
                curr = curr.prev
        return curr.val
        
    #references addAtIndex to add a node with given value
    #at the beginning of list (given index 0)
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)

    #references addAtIndex to add a node with given value
    #at the end of the list (given index 0)
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    #adds a node of given value at the given index
    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        NewNode = Node(val)
        if index == 0:
            if self.size == 0:
                self.head = NewNode
                self.tail = NewNode
            else:
                NewNode.next = self.head
                self.head.prev = NewNode
                self.head = NewNode
        elif index == self.size:
            if self.size == 0:
                self.head = NewNode
                self.tail = NewNode
            else:
                self.tail.next = NewNode
                NewNode.prev = self.tail
                self.tail = NewNode
        else:
            curr = self.head
            for i in range(index):
                curr=curr.next
            NewNode.next = curr
            NewNode.prev = curr.prev
            curr.prev.next = NewNode
            curr.prev = NewNode
        
        self.size += 1

    #deletes the node at the given index
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        curr = self.head
        if index == 0:
            if self.size == 1:
                self.head = 0
                self.tail = 0
            else:
                self.head = curr.next
                self.head.prev = None
        elif index == self.size -1:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            for i in range(index-1):
                curr = curr.next
            curr.next = curr.next.next
            curr.next.prev = curr
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)