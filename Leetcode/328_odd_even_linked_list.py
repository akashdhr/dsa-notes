# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Below solution uses O(N) extra space
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode()
        newCur = newHead
        even = []
        odd = []
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            # if current node is odd
            if cnt%2 != 0:
                odd.append(cur.val)
            # if current node is even
            else:
                even.append(cur.val)
            cur = cur.next
        for i in odd:
            newNode = ListNode(i)
            newCur.next = newNode
            newCur = newNode
        for i in even:
            newNode = ListNode(i)
            newCur.next = newNode
            newCur = newNode
        return newHead.next
# Below solution uses O(1) extra space
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = oddHead = ListNode()
        even = evenHead = ListNode()
        cur = head
        cnt = 0
        while cur:
            cnt += 1
            # If current node is odd
            if cnt % 2 != 0:
                odd.next = cur
                odd = cur
            # If current node is even
            else:
                even.next = cur
                even = cur
            cur = cur.next
        even.next = None
        odd.next = evenHead.next
        return oddHead.next

        