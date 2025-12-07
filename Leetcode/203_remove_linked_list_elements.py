# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = head
        cur = dummy = ListNode()
        while temp:
            if temp.val != val:
                cur.next = temp
                cur = cur.next
            temp = temp.next
        cur.next = None
        return dummy.next