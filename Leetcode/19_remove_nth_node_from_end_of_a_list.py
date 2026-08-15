# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # calculate total length
        # subtract the value n = l-n
        # iterate to (l-n)th node and delete it

        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        
        x = length - n
        if x == 0:
            return head.next
        i = 0
        cur = head
        while cur:
            i += 1
            if i == x:
                break
            cur = cur.next
        cur.next = cur.next.next
        return head
        
        
#time complexity: O(n) where n is the number of nodes in the linked list.
#space complexity: O(1) since we are modifying the list in place and not using any additional data structures to store the nodes.