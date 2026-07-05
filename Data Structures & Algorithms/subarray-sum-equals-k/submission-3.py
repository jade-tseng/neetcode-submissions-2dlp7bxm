class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        freq = {0: 1}
        res = 0

        for i, num in enumerate(nums):
           prefix += num
           diff = prefix - k
           # READ how many earlier prefixes = diff
           res += freq.get(diff, 0)
           # WRITE: record current prefix
           freq[prefix] = freq.get(prefix, 0) + 1
        
        return res
            