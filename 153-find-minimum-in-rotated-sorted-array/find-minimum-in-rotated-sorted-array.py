class Solution:
    def findMin(self, nums: list[int]) -> int:
        result=nums[0]
        for i in range(len(nums)):
            if nums[i]<result:
                result=nums[i]
        return result