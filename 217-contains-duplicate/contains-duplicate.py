class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        for i in nums:
            if d[i]>1:
                return True
        return False










        # d={}
        # for i in nums:
        #     d[i]=d.get(i,0)+1
        # for i in nums:
        #     if d[i]>1:
        #         return True
        # return False

        # s=set()
        # for i in nums:
        #     if i not in s:
        #         s.add(i)
        #     else:
        #         return True
        # return False
        