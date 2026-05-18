class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_Palindrome(left: int, right: int) -> bool: 
            while left < right: 
                if s[left] != s[right]: 
                    return False 
                else: 
                    left += 1
                    right -= 1
            return True 

        left = 0
        right = len(s) - 1
        while left < right: 
            if s[left] != s[right]: 
                return is_Palindrome(left + 1, right) or is_Palindrome(left, right - 1)
            else: 
                left += 1
                right -= 1
        return True