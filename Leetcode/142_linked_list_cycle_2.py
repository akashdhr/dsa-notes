# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# O(N) memory as we are using hashset
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen = set()
        cur = head
        while cur:
            if cur in seen:
                return cur
            else:
                seen.add(cur)
            cur = cur.next

# O(1) memory as we are using slow, fast pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        # Detect cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None # No cycle detected
        # fast has travelled 2 * the same distance as slow
        # To check where the loop starts, reset the slow pointer and check where they meet again with fast (same speed as slow)
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow 
        