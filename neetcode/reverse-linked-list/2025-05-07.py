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
        prev = None

        while current:
            nextStore = current.next
            current.next = prev
            prev = current
            current = nextStore

        return prev


