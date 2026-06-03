class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #use kadane algorithm set two pointers 
        currsum,maxsum= 0, nums[0]
        #reset the sliding window if value goes begative
        for n in nums:
            if currsum<0:
                currsum=0
            currsum+=n
            maxsum= max(maxsum,currsum)
        return maxsum
        #update max and return the sum of larget sub array
        