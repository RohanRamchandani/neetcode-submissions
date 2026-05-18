class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        max_area = 0

        while left < right: 
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(area, max_area)

            # You move the pointer which is smaller than the other pointer 
            if heights[left] < heights[right]: 
                left += 1
            else: 
                right -= 1
        return max_area

        # Time Complexity: O(n) time complexity
        # Space Complexity: O(1) space complexity