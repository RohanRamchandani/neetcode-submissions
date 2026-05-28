class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Using a HashMap here will cost us O(n + m) time and also O(n) space
        result = []
        map = {}
        for i in nums: 
            if i not in map: 
                map[i] = 1
            else: 
                map[i] += 1
        for num in map: 
            if map[num] > len(nums) // 3: 
                result.append(num) 
        return result 