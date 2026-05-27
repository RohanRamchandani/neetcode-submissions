class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # For nums1, the length of it is (m+n), where m is the actual length where you wil get numbers and the last n will be zeros, now your job is to sort nums1 and also take nums from nums2, and replace the zeros with the sorted numbers 
        # The question is how can I shift the elements to the right so I can replace the zeros? 
        for i in range(n): 
            nums1[m+i] = nums2[i]
        nums1.sort()