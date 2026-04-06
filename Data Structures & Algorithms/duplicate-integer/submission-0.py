class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()

        for i in nums:
            dupes.add(i)

        if len(dupes) == len(nums):
            return False
        else:
            return True