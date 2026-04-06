# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # store nodes in a hash set
        store = set()
        curr = head 

        while curr:
            store.add(curr)
            curr = curr.next
            if curr in store:
                return True
        
        return False