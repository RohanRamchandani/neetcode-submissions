class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)): 
            # Skip the duplicate first element from the list 
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            
            key = nums[i]
            left = i+1
            right = len(nums) - 1

            while left < right: 
                total = key + nums[left] + nums[right]
                if total == 0: 
                    res.append([key, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip all left duplicates 
                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1
                    
                    # Skip all right duplicates 
                    while right > left and nums[right] == nums[right + 1]: 
                        right -= 1
                elif total < 0: 
                    left += 1
                else: 
                    right -= 1
        return res
                