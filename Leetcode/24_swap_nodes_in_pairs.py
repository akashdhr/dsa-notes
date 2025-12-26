# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = ListNode()
        cur.next = head
        prev = cur
        
        while cur.next and cur.next.next:
            first = cur.next
            second = cur.next.next

            # Swap
            first.next = second.next
            second.next = first
            cur.next = second

            cur = first
        return prev.next