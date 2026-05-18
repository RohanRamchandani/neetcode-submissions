class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # You are being given an array of integers and you are supposed to return the indices of the element where two elements added should be == to the target 
        hash_map = {}
        for index, value in enumerate(nums): 
            diff = target - value 
            if diff in hash_map: 
                return [hash_map[diff], index]
            hash_map[value] = index