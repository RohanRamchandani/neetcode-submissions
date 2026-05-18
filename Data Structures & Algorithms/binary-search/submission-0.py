class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Your middle will always change so you gotta find a way to update it 
        low, high = 0, len(nums) - 1

        while low <= high: 
            middle = (low + high) // 2
            if nums[middle] == target: 
                return middle 
            elif target > nums[middle]: 
                low = middle + 1
            else: 
                high = middle - 1
        return -1