# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return (head.next != None)
        
        s, f = head, head.next

        while s and f.next:
            s = s.next
            f = f.next.next

            if s == f:
                return True
        
        return False
