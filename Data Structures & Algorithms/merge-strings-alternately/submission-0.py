class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = "" 
        leftWord1 = 0
        leftWord2 = 0 

        while leftWord1 < len(word1) and leftWord2 < len(word2): 
            result += word1[leftWord1]
            result += word2[leftWord2]

            leftWord1 += 1
            leftWord2 += 1
        
        if len(word1) > len(word2): 
            result += word1[leftWord1:]
        else: 
            result += word2[leftWord2:]
        
        return result 