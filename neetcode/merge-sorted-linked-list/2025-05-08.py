# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2
        new = ListNode(val=0)
        currNew = new

        while l1 and l2:
            if l1.val < l2.val:
                currNew.next = l1
                l1 = l1.next
            else:
                currNew.next = l2
                l2 = l2.next
            
            currNew = currNew.next
        
        if l1:
            currNew.next = l1
        if l2:
            currNew.next = l2
        
        return new.next

