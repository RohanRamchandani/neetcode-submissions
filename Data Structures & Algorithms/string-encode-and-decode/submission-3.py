class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs: 
            res += str(len(i)) + "#" + i
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): 
            j = i 
            # read length 
            while s[j] != "#": 
                j += 1
            
            length = int(s[i:j])

            j += 1
            temp = s[j:j+length]
            res.append(temp)

            i = j + length
        return res