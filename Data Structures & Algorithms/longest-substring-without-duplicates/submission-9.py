class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        max_length = 0
        seen = set()
        
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        seen.add(s[l]) # "au" 1 2 s[l:r] s[0:1] a

        while r < len(s):
            if s[r] in seen: 
                max_length = max(max_length, len(s[l:r]))
                seen = set()
                l += 1
                seen.add(s[l])
                r = l + 1

            else: 
                seen.add(s[l])
                seen.add(s[r])
                
                r += 1

                max_length = max(max_length, len(s[l:r]))
        
        return max_length
