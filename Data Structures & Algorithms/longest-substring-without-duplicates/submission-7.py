class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)): 
            seen = set()
            for j in range(i, len(s)): 
                if s[j] not in seen: 
                    seen.add(s[j])
                else: 
                    break
            res = max(res, len(seen)) 
        return res