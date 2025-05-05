# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        current = head
        prevVal = None

        while current:
            nextVal = current.next
            current.next = prevVal
            prevVal = current
            current = nextVal

        return prevVal

            
