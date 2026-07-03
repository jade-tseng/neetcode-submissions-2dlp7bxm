class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        naive approach is O(n*2) = loop through all paris
        hashmap solution is O(n) time, O(n) space, optimal if nums is unsorted
        if nums is sorted already, we can use 2 pointers, for O(n) time and O(1) space
        sorting nums is O(n log n) so here this solution is o(n log n)
        """
        seen = {}

        for i, n in enumerate(nums):
            seen[n] = i
        
        for i, n in enumerate(nums):
            comp = seen.get(target - n, None)
            if comp and comp!= i:
                return [i, comp]
