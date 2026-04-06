class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums[i] + nums[j] + nums[k] == 0
        # -nums[i] = nums[j] + nums[k] == 0
        result = []
        nums = sorted(nums)
        
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[j] + nums[k]
                if total == target:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif total < target:
                    j += 1
                else:
                    k -= 1
                
        return result


            # get nums[i] = - (nums[j] + nums[k]) == 0
            # for each index i , calculate j, k pairs without duplicates
            # which algorithm finds j, k pairs? two pointers
            # if current sum num[j] + nums[k] < target: increase value of sum by incrementing j
            # elif num[j] + nums[k] > target: decrease by decrementing k pointer
            # how to deal with duplicates?
            # because the array is sorted, so duplicates are always adjacent. You just slide past them !!
            # when sum == target, add to result
            # move j,k pointers until j < k and pairs are repeated .. ?

                    