# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # put list in an array helper func
        def to_array(head):
            result = []
            while head:
                result.append(head.val)
                head = head.next
            return result
        
        # put list into array:
        l1 = to_array(list1)
        l2 = to_array(list2)
        result = l1 + l2
        
        # sort the array:
        result.sort()

        # converting back to LinkedList:
        ll = ListNode()
        curr = ll
        for val in result:
            curr.next = ListNode(val)
            curr = curr.next
        return ll.next