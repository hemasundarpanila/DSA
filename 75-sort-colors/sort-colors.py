class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp,low,high=0,0,len(nums)-1
        while temp<=high:
            if nums[temp]==0:
                nums[temp],nums[low]=nums[low],nums[temp]
                temp+=1
                low+=1
            elif nums[temp]==1:
                temp+=1
            else:
                nums[high],nums[temp]=nums[temp],nums[high]
                high-=1
        return nums