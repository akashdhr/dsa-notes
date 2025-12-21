# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # First check the length
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        # If odd then return the (length + 1)/2 th element
        # If even then reutn the (length)/2 + 1 th element
        # Even length
        if length % 2 == 0:
            target = (length // 2) + 1
        # Odd length
        else:
            target = (length + 1) // 2
        i = 0
        cur = head
        while cur:
            i += 1
            if i == target:
                return cur
            cur = cur.next
        