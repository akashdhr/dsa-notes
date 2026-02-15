# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the total length first
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        toDelete = length - n
        i = 0
        cur = head
        if toDelete == 0:
            return head.next
        while cur:
            i += 1
            if i == toDelete:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head

#time complexity: O(n) where n is the number of nodes in the linked list.
#space complexity: O(1) since we are modifying the list in place and not using any additional data structures to store the nodes.