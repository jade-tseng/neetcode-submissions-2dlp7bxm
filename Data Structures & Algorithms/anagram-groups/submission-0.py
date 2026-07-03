class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = set()
        res = {}

        for elem in strs:
            e = "".join(sorted(elem))
            
            if e in words:
                res[e].append(elem)
            else:
                res[e] = [elem]

            words.add(e)
        
        return list(res.values())


