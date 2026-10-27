class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        d={}
        k=0
        for i in nums:
            if i not in d:
                d[i]=1
                nums[k]=i
                k=k+1
        return k

                

        # l=[]
        # for i in range(len(nums)):
        #     if nums[i]