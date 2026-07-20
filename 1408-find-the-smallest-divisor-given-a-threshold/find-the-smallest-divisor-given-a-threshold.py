
class Solution:
    def ceil(self,nums,divisor,n):
        totalsum=0
        for i in range(n):
            totalsum+= (nums[i]+divisor-1)//divisor
        return totalsum
            

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        low,high= 1,max(nums)
        if n>threshold:
            return -1
        while low<=high:
            mid = low+(high-low)//2
            if self.ceil(nums,mid,n)<=threshold:
                high=mid-1
            else:
                low=mid+1
        return low

      


        