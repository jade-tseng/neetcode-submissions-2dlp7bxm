class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        s = s.lower()
        s = "".join(c for c in s if c.isalnum())

        return s == s[::-1]