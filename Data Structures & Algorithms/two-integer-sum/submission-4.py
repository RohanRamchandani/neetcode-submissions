class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # You are being given an array of integers and you are supposed to return the indices of the element where two elements added should be == to the target 
        for i in range(len(nums)): 
            for j in range(i + 1, len(nums)): 
                if nums[i] + nums[j] == target: 
                    return [i, j]
        return []