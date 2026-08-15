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
        # break the list from the middle
        # reverse the second half
        # merge the two
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None #break the link of second half from the first half
        prev = None
        # reverse the second half
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        # reversed second half is ready. time to merge with the first half
        first = head
        second = prev
        # iterating on second because it will be shorter or equal to the first half
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        
        return head


    
#time complexity: O(n) where n is the number of nodes in the linked list.
#space complexity: O(1) since we are modifying the list in place and not using any additional data structures to store the nodes.