class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # For nums1, the length of it is (m+n), where m is the actual length where you wil get numbers and the last n will be zeros, now your job is to sort nums1 and also take nums from nums2, and replace the zeros with the sorted numbers 
        # The question is how can I shift the elements to the right so I can replace the zeros? 
        last = m + n - 1
        i = m - 1
        j = n - 1

        while j >= 0: 
            if i >= 0 and nums1[i] > nums2[j]: 
                nums1[last] = nums1[i]
                i -= 1
                last -= 1
            else: 
                nums1[last] = nums2[j]
                j -= 1
                last -= 1