# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        len = 1

        cur_node = head
        while (cur_node.next != None):
            len += 1
            cur_node = cur_node.next
        
        index = len / 2 if (len % 2 == 0) else floor(len / 2)

        starting = new
        original = head

        for i in range (len):
            if i == index:
                starting.val = original.val

            elif i > index:
                starting.next = ListNode(original.val, None)
                starting = starting.next

            original = original.next
            
        return new
        