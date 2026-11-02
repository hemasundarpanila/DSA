class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        mf=le=r=0
        d={}
        while r<len(fruits):
            d[fruits[r]]=d.get(fruits[r],0)+1
            while len(d)>2:
                d[fruits[le]]=d.get(fruits[le])-1
                if d[fruits[le]]==0:
                    d.pop(fruits[le])
                le+=1
            mf=max(mf,r-le+1)
            r+=1
        return mf