# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 두칸씩 가면 원래애의 중간지점을 찾을수있으니까
        old = head
        new = head

        while (old and old.next):
            old = old.next.next
            new = new.next

        return new
        