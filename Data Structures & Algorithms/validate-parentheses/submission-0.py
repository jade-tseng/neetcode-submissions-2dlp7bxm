from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        OpentoClose = {'{' : '}', '[' : ']', '(' : ')'}

        # we add chars in string to a stack if it is open bracket [ { [ ...
        for c in s:
            if c in OpentoClose: # if its an open bracket:
                stack.append(c) # appends stack = ([{
            else: # its not an open bracket but closed one in s:
                # check if closed matches open 
                if stack and OpentoClose[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
                
                
