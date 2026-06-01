class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pivot= 0
        #find pivot
        for i in range(n-1,0,-1):
            if nums[i-1]<nums[i]:
                pivot= i
                break
        if pivot==0:
            nums.reverse()
            return
            
        #then swap first number>pivot
        swap = n-1
        while nums[pivot-1]>=nums[swap]:
            swap-=1

        #swap
        nums[pivot-1],nums[swap]= nums[swap],nums[pivot-1]
        #reverse the array after swap
        nums[pivot:]= reversed(nums[pivot:])

        