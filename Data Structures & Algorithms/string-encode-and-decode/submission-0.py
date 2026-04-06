class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in strs:
            l = len(i)
        
        s = ''.join([str(len(i)) + "#" + str(i) for i in strs])

        return s

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            # find the # to read the length
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # grab exactly 'length' characters after the #
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result
