# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        second = slow.next
        slow.next = None # break the link
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # Merge the list
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next  = second
            second.next = temp1
            first = temp1
            second = temp2

#time complexity: O(n) where n is the number of nodes in the linked list.
#space complexity: O(1) since we are modifying the list in place and not using any additional data structures to store the nodes.