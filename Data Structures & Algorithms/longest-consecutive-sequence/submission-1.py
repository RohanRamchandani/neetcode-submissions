class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        store = set(nums)

        for num in nums: 
            if num - 1 not in store: 
                length = 1
                current = num 

                while current + 1 in store: 
                    length += 1
                    current += 1
                
                longest = max(length, longest)
        return longest