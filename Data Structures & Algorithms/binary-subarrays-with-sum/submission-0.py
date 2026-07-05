class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        """
        prefix sum :
        nums [1, 0, 1, 0, 1], goal = 2
        pref [1, 1, 2, 2, 3]

        diff = prefix - goal
        """

        freq = {0: 1} # seed empty prefix
        goals = 0
        prefix = 0

        for n in nums:
            prefix += n
            diff = prefix - goal
            # read:
            goals += freq.get(diff, 0)
            # write, record in freq:
            freq[prefix] = freq.get(prefix, 0) + 1

        return goals
