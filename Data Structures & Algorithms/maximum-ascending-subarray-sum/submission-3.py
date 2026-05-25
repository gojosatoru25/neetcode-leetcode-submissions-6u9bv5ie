class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        if not nums: return 0
        
        res = curr = nums[0]
        # Start loop from 1 instead of 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                # If strictly ascending, add to current sum
                curr += nums[i]
            else:
                # Sequence broken, reset current sum to current number
                curr = nums[i]
                
            res = max(res, curr)
            
        return res
        