class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        nums = sorted((value, index) for index, value in enumerate(nums))
        while left < right:
            total = nums[left][0] + nums[right][0]
            if total == target:
                return nums[left][1], nums[right][1]
            elif total < target:
                left += 1
            else:
                right -= 1


        # left=0
        # right=len(nums)-1
        # nums.sort()
        # while left<right:
        #     if nums[left]+nums[right]==target:
        #         return left,right
        #     elif nums[left]+nums[right]<target:
        #         left+=1
        #     else:
        #         right-=1
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return i,j
        