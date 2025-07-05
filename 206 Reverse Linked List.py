#problem 206: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #this solution uses recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: #base case
            return None
        
        newHead = head

        if head.next: #if there is a next node
            newHead = self.reverseList(head.next) #recursive call 
            head.next.next = head

        head.next = None
        return newHead