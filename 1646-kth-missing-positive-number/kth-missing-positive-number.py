class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n= len(arr)
        low,high= 0 ,n-1
        while low<=high:
            mid= low+(high-low)//2
            missing= arr[mid]-(mid+1)
            if missing<k:
                low= mid +1
            else:
                high= mid-1
        return high+1+k     