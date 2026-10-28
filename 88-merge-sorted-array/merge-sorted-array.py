class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        l = r = 0
        result=[]
        while l<m and r<n:
            if nums1[l]<=nums2[r]:
                result.append(nums1[l])
                l=l+1
            else:
                result.append(nums2[r])
                r=r+1
        while l<m:
            result.append(nums1[l])
            l=l+1
        while r<n:
            result.append(nums2[r])
            r=r+1
        for i in range(m+n):
            nums1[i]=result[i]
        return nums1

      
