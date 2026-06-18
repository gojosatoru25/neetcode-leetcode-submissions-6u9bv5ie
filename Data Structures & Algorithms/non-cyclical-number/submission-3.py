class Solution:
    def isHappy(self, n: int) -> bool:
        a=set()
        while n!=1 and n not in a:
            a.add(n)
            n= sum(int(digits)**2 for digits in str(n))
        return n==1

        