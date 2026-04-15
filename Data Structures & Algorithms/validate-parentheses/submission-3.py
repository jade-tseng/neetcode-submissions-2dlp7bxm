from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # we use stack to put chars of s in stack
        # we use a dict to keep track of which brackets belong to each other

        q = deque()
        brackets = {'{':'}', '(': ')', '[':']'}

        for c in s:
            if c in brackets: # if c is opening bracket (key)
                q.append(c) # q contains all opening brackets
                # so now, q.pop() should give us 

            else:
                if not q:
                    return False # case in which there is }]) but no opening bracket to match, ie. ()]
                
                b = q.pop()
                if c != brackets[b]: # if mismatch
                    return False
        
        return len(q) == 0

                
        