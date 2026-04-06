class Solution:
    def findMin(self, nums: List[int]) -> int:
        # initialize l, u as first and last index of array:
        min, max = 0, len(nums) - 1

        while min < max:
            mid = (min + max) // 2
            # if l < nums[mid] then we search right
            # if nums[mid] < r then we search left
            # if nums[l] < nums[mid]: 
            # if nums[mid] < nums[r]:
            if nums[mid] > nums[max]:  #rotation is in the right half, min is right of mid. [3,4,5,6,1,2]
                min = mid + 1 # becomes 6
            else: # left is unsorted, we search left, right is sorted
                max = mid

        return nums[min]



