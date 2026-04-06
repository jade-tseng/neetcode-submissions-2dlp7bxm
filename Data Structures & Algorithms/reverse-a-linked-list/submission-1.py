# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init [0, 1, 2, 3]
        prev = None
        curr = head # 0
        while curr:
            next_node = curr.next # 1
            curr.next = prev # 1
            prev = curr # 0
            curr = next_node #1
        return prev
