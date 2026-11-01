class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k=2
        for i in range(2,len(nums)):
            if nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k=k+1
        return k















        # d={}
        # l=[]
        # for i in nums:
        #     d[i]=d.get(i,0)+1
        #     if d[i]==2 or d[i]==1:
        #         l.append(i)
        # return l
