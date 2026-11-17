class Solution:
    def findMin(self, nums: list[int]) -> int:
        start=0
        end=len(nums)-1
        while start<end:
            mid=(start+end)//2
            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid
        return nums[start]



        # result=nums[0]
        # for i in range(len(nums)):
        #     if nums[i]<result:
        #         result=nums[i]
        # return result

