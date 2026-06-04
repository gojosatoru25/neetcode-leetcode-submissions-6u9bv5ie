class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #set a fast and a slow pointer 
        slow, fast = 0,0
        while True:
            #slow pointer with 1 step and fast with two step
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast :
                #setting fast as 0 so that we can reset the cycle
                fast = 0
                break

        while True:
            slow = nums[slow]
            fast= nums[fast]
            if slow == fast:
                return slow
            
        