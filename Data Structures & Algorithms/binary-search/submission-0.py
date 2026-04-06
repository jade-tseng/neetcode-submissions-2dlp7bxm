class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid # index 3, val 2
            elif nums[mid] < target:
                l = mid + 1 # l = index 4, val 4
            else:
                r = mid - 1 # r =
        
        return -1
