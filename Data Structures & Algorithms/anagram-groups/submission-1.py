class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for elem in strs:
            e = "".join(sorted(elem))
            if e in res:
                res[e].append(elem)
            else:
                res[e] = [elem]
        
        return list(res.values())


