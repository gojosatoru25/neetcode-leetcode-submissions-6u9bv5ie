class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        s = list(str(abs(x)))
        l, r = 0, len(s) - 1
        
        while l < r:
            s[l], s[r] = s[r], s[l]  # Fixed: Added the missing comma here
            l += 1
            r -= 1
        
        reverse_1 = sign * int("".join(s))
        
        # Fixed: Changed reversed_x to reverse_1 to match your variable name
        if reverse_1 < -2**31 or reverse_1 > 2**31 - 1:
            return 0
            
        return reverse_1
