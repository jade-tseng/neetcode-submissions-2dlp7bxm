import math

class Solution:
    def time_taken(self, piles: List[int], k: int) -> int:
        """time taken to eat bananas, ie."""
        j = 0
        for i in piles:
            j += math.ceil(float(i) / k) # assuming round up
        return j

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # min = total bananas / hours you have
        min_k = math.ceil(float(sum(piles)) / h) # 10 / 9 => 2 ///// 62 / 4 => 16
        max_k = max(piles) # largest number in piles: 4 //// 25

           # for binary search, we need middle:
        while min_k <= max_k:
            mid = (min_k + max_k) // 2 # ex2: 20.5 21.5
            j = self.time_taken(piles,mid)
            # if time taken == hours available, return 
            if j <= h: # search lower bound:
                result = mid
                max_k = mid - 1
        # if time taken to eat bananas is less time than hours available, we can have more time
            else: # j > h
                min_k = mid + 1
        return mid