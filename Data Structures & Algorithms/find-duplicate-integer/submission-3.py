class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for left in range(len(nums)): 
            count = 0
            for right in range(len(nums)): 
                if nums[left] == nums[right]: 
                    count += 1
                    if count >= 2: 
                        return nums[left]
                