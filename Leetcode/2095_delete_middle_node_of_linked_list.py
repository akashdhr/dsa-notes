# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# This is a 2 pass solution
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Find length of the list
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        if length == 1:
            return None
        mid = length//2
        cnt = 0
        cur = head
        while cur:
            if (cnt+1) == mid:
                cur.next = cur.next.next
                break
            cur = cur.next
            cnt += 1
        return head
                
# This is a 1 pass solution using slow and fast pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # slow is at middle
        prev.next = slow.next

        return head
