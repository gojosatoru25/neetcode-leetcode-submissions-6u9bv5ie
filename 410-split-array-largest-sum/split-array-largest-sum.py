class Solution:
    def max_sum(self,nums,min_sum,n):
        count_subarray=1
        sums=0
        for i in range(n):
            if nums[i]+sums<=min_sum:
                sums+=nums[i]
            else:
                count_subarray+=1
                sums= nums[i]
        return count_subarray
    def splitArray(self, nums: List[int], k: int) -> int:
        n= len(nums)
        low= max(nums) 
        high= sum(nums)
        if k>n:
            return -1
        while low<=high:
            mid= low+(high-low)//2
            if self.max_sum(nums,mid,n)<=k:
                high= mid-1
            else:
                low= mid+1
        return low
        