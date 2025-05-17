# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        
        l, r = dummyNode, dummyNode.next
        nextN = l.next.next

        for i in range(n):
            r = r.next
        
        while r:
            l = l.next
            r = r.next
            nextN = l.next.next
        
        l.next = nextN

        return dummyNode.next

