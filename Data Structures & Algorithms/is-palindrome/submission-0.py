class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            #skip over non-alphanumerical chars
            while left < right and not s[left].isalnum():
                left += 1
        
            while left < right and not s[right].isalnum():
                right -= 1
            
            # compare chars in lowercase
            if s[left].lower() != s[right].lower():
                return False
            
            #move pointers towards center
            left += 1
            right -= 1

        return True
