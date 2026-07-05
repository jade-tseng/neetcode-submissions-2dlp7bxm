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
            seen = set()
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])

                if target in seen:
                    found.add((nums[i], target, nums[j]))
                    
                seen.add(nums[j])
        return [list(f) for f in found]
