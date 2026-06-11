class Solution:
    def isPalindrome(self, s: str) -> bool:
        n= len(s)
        cleaned = "".join([char.lower() for char in s if char.isalnum()])
        def check_palindrome(i: int) ->bool:
            n= len(cleaned)
            if i>=n//2:
                return True
            if cleaned[i]!= cleaned[n-i-1]:
                return False
            return check_palindrome(i+1)
        return check_palindrome(0)

       
        
        