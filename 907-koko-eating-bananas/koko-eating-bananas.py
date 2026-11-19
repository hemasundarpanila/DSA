class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # def timetaken(piles,h):
        def timetaken(piles,mid):
            t=0
            for i in piles:
                t+=i//mid
                if (i%mid)!=0:
                    t+=1
            return t
        start=1
        end=max(piles)
        ans=max(piles)
        while start<=end:
            mid=(start+end)//2
            tt=timetaken(piles,mid)
            if tt<=h:
                ans=mid
                end=mid-1
            else:
                start=mid+1
        return ans
        
                
            
