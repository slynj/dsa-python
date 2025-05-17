# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        saveHead = ListNode()
        saveHead.next = head

        prev = None
        NthCheck = head
        curr = head

        while curr:
            for i in range(n):
                NthCheck = NthCheck.next
            
            if not NthCheck:
                if not prev:
                    return curr.next
                prev.next = curr.next
                break

            prev = curr
            curr = curr.next
            NthCheck = curr
        
        return head
        

            


            



