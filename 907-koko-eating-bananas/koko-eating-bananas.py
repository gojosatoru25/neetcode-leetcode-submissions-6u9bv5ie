import math
class Solution:
    def minhours(self, piles,speed):
        totalhours=0
        for bananas in piles:
            totalhours+= math.ceil(bananas/speed)
        return totalhours
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxp= max(piles)
        low,high= 1,maxp
        while low<=high:
            mid= low+(high-low)//2
            totalhours= self.minhours(piles,mid)
            if totalhours<= h:
                high= mid-1
            else:
                low=mid+1
        return low

        