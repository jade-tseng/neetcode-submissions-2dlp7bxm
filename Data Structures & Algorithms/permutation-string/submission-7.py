from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # frequency counter for s1:
        freq1 = Counter(s1)
        
        # freq = {}
        # for s in s1:
        #     freq[s] = freq.get(s, 0) + 1
        
        k = len(s1)
        window = Counter(s2[0:k])

        if window == freq1:
                return True
                
        # s2[0:k] -> 
        for r in range(len(s2) - k):
            print(window)

            print(r)
            window[s2[r+k]] += 1 #window.update(s2[r+k]) 
            window[s2[r]] -= 1
            if window == freq1:
                return True


        return False



