# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            temp = curr.next #store the next nodes in a temp var
            curr.next = prev #store the prev node in the next transition for the current node
            prev = curr # store the curr node as prev
            curr = temp #store the next node as the curr node

        return prev #return the last remaining node which will be the head of the newly ordered list
            

        