class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Need to solve in O(1) space complexity (in-place algorithm)
        index = 0
        for i in range(len(nums)): 
            if nums[i] != val: 
                nums[index] = nums[i]
                index += 1
        return index