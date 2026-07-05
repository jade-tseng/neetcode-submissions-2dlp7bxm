class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:                  
        # we sort nums
        # use a 'found' set for triplets so you don't repeat any
        # loop through nums [outer loop]
        # seen set for numbers we've seen at every fixed nums[i] (to find the 2 complement numbers)
        # inner loop to go from every i
        # define what we're looking for: third number: target, nums[i], nums[j]
        # if we find it in seen: we add the triplet to found
        # we add number to what we've seen 
        # return triplets
        nums.sort()
        found = set()

        for i in range(len(nums)):
        
            j, k = i + 1, len(nums) - 1

            while j < k:
                if nums[i] == -(nums[j] + nums[k]):
                    found.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif nums[i] < -(nums[j] + nums[k]):
                    j += 1
                else:
                    k -= 1

        return [list(f) for f in found]
