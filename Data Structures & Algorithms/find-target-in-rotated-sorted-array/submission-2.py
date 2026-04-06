class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # initialize pointers at 0 and end of nums
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            elif nums[r] > nums[mid]: # if r > mid, right part is sorted, so search left
                if nums[mid] <= target <= nums[r]: # target in sorted range, upper
                    # search right:
                    l = mid + 1
                else:
                    r = mid - 1
            else: # nums[r] <= nums[mid] so left is sorted, search right. mid to r
                if nums[l] <= target <= nums[mid]: 
                    # search left
                    r = mid - 1
                else:
                    l = mid + 1 # search right
        # if target not in nums:
        return -1

