# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = list1
        t2 = list2
        cur = head = ListNode()
        while t1 and t2:
            if t1.val <= t2.val:
                cur.next = t1
                t1 = t1.next
            else:
                cur.next = t2
                t2 = t2.next
            cur = cur.next
        if t1:
            cur.next = t1
        if t2:
            cur.next = t2
        return head.next

# time complexity: O(n + m) where n and m are the number of nodes in the two linked lists.
# space complexity: O(1) since we are using only a constant amount of space to store the current and previous nodes.