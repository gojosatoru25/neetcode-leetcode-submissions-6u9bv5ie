class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1,n2= len(nums1),len(nums2)
        merged=[]
        i,j=0,0
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                merged.append(nums1[i])
                i+=1
            else:
                merged.append(nums2[j])
                j+=1
        while i<n1:
            merged.append(nums1[i])
            i+=1
        while j<n2:
            merged.append(nums2[j])
            j+=1
        n3= n1+n2
        if n3%2==1:
            return merged[n3//2]
        else:
            return (merged[n3//2]+ merged[(n3//2-1)])/2

        