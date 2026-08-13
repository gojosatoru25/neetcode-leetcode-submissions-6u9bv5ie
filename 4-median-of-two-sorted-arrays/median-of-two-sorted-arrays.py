class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1,n2= len(nums1),len(nums2)
        n= n1+n2
        i,j=0,0
        ind2= n//2
        ind1= ind2-1
        count=0
        ind1el,ind2el=-1,-1
        while i<n1 and j<n2:
            if nums1[i]<nums2[j]:
                if count == ind1:
                    ind1el= nums1[i]
                if count == ind2:
                    ind2el=nums1[i]
                count+=1
                i+=1
            else:
                if count == ind1:
                    ind1el= nums2[j]
                if count== ind2:
                    ind2el= nums2[j]
                count+=1
                j+=1
        while i<n1:
            if count == ind1:
                ind1el= nums1[i]
            if count == ind2:
                ind2el=nums1[i]
            count+=1
            i+=1
        while j<n2:
            if count == ind1:
                ind1el= nums2[j]
            if count == ind2:
                ind2el= nums2[j]
            count+=1
            j+=1
        if n%2==1:
            return ind2el
        else:
            return (ind2el+ind1el)/2

        