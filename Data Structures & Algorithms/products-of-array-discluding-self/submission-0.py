class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    # [1, 2, 8, 48]
    # [48, 48, 24  ,6]  
        l = len(nums)
        cum_prod_left = [0] * l
        cum_prod_right = [0] * l
        answer = [0] * l
        cum_prod_left[0] = nums[0]
        cum_prod_right[l-1] = nums[l-1]

        for i in range(1, l):
            cum_prod_left[i] = cum_prod_left[i - 1] * nums[i]
            cum_prod_right[l-i-1] = cum_prod_right[l-i] * nums[l-i-1]

        answer[0] = cum_prod_right[1]
        answer[l-1] = cum_prod_left[l-2]

        for i in range(1, l-1):
            answer[i] = cum_prod_left[i-1] * cum_prod_right[i + 1]
        
        return answer


