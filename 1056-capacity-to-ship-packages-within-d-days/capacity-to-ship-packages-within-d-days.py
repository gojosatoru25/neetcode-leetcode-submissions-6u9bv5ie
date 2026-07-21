class Solution:
    def dday(self,weights, capacity):
        day=1
        total_weight=0
        for i in weights:
            if total_weight+i>capacity:
                day+=1
                total_weight=i
            else:
                total_weight+=i
        return day
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high= sum(weights)
        while low<=high:
            mid= low+(high-low)//2
            if self.dday(weights,mid)<=days:
                high= mid-1
            else:
                low=mid+1
        return low
                                                                                                                                                                        
                                     