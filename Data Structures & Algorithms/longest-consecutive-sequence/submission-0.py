class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        store = set(nums)

        for num in nums: 
            streak = 0
            curr = num
            while curr in store: 
                streak += 1
                curr += 1
            result = max(streak, result)
        
        return result