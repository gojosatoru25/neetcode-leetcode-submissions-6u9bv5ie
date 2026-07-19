class Solution:
    def ispossible(self,bloomDay,day,m,k):
        count=0
        nobouquets=0
        for bloom in bloomDay:
            if bloom<=day:
                count+=1
                if count==k:
                    nobouquets+=1
                    count= 0
            else:
                count=0
        return nobouquets>=m
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n= len(bloomDay)
        total_flowers= m*k
        if total_flowers>n:
            return -1
        low,high= min(bloomDay),max(bloomDay)
        while low<=high:
            mid= low+(high-low)//2
            if self.ispossible(bloomDay,mid,m,k):
                high=mid-1
            else:
                low= mid+1
        return low 
                
        