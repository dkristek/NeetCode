#problem: https://leetcode.com/problems/merge-two-sorted-lists/description/
#this problem asks to merge two sorted, linked lists
#I solved this problem recursively

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#solution using recursion
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #instead of creating a new list to return we will just move nodes from one list to another in sorted order
        #until one list is empty

        if list1 is None: #if list1 doesn't exist/is empty we can just merge the rest of list2 as its already sorted
            return list2
        if list2 is None: #if list2 doesn't exist/is empty we can just merge the rest of list1 as its already sorted
            return list1
        
        #recurrence functions
        #to sort the list
        if list1.val <= list2.val: #will place list1.val first 
               list1.next = self.mergeTwoLists(list1.next, list2) #recurrence, feeds in list1 starting at the next node
               return list1
        else:
            list2.next = self.mergeTwoLists(list2.next, list1) #recurrence, feeds in list2 starting at the next node
            return list2

#solution using iteration
#this solution was easier for me to intuit on my own
#I need to improve on my understanding of recursion techniques. they still don't come naturally to me
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node so we don't insert into an empty list
        dummy = ListNode()
        tail = dummy

        #while loop to continue as long as both lists have nodes
        while list1 and list2:
            if list1.val < list2.val: #list1 val is smaller adds that val to tail of list and moves onto the next val in list1
                tail.next = list1
                list1 = list1.next
            else:
                #list2 val is smaller or equal adds that val to tail of list and moves onto the next val in list2
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        #one of the lists does have nodes still
        if list1:
            tail.next = list1 #merges rest of list1 onto merged list (original lists are sorted already)
        elif list2:
            tail.next = list2 #merges rest of list2 onto merged list (original lists are sorted already)
        return dummy.next
