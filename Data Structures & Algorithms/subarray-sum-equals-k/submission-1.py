import numpy as np

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = np.cumsum(nums)
        m = {}
        for i, ele in enumerate(prefix_sum):
            l = m.get(int(ele))
            if l:
                l.append(i)
            else:
                l = [i]
                m[int(ele)] = l
        answer = 0
        for i, ele in enumerate(prefix_sum):
            if ele == k:
                answer+= 1
            comp = int(ele) - k
            l = m.get(comp)
            if l:
                for j in l:
                    if j < i:
                        answer += 1
        return answer
