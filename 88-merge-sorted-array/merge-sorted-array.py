class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        result = []
        r = l = 0
        while r < m and l < n:
            if nums1[r] <= nums2[l]:
                result.append(nums1[r])
                r += 1
            else:
                result.append(nums2[l])
                l += 1
        while r < m:
            result.append(nums1[r])
            r += 1
        while l  < n:
            result.append(nums2[l])
            l += 1
        for i in range(m + n):
            nums1[i] = result[i]
        return nums1
