class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs: # for every string in the list of strings
            result.append(str(len(s))) # take length of string
            result.append("#") # add a delimiter sign
            result.append(s) # add it to the result
        return "".join(result) # creates an encoded string.

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res