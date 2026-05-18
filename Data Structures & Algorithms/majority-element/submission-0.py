class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        hashMap = {}
        for i in nums: 
            if i in hashMap: 
                hashMap[i] += 1
            else: 
                hashMap[i] = 1
        
        for i in hashMap: 
            if hashMap[i] > len(nums) // 2: 
                count = i
        
        return count 