class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # The keyword here is "elements of the same color are grouped together and arranged in the order of 0 -> 1 -> 2, so this shows we want to sort it in non-descreasing order, not ascending order, so for example 1 >= 1, should also be sorted, side by side"
        # We need O(1) space complexity 
        for i in range(len(nums)): 
            for j in range(i+1, len(nums)): 
                if nums[j] <= nums[i]: 
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp