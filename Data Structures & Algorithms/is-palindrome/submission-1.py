class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())

        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
            
        return True