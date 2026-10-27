class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1

        # for i in range(len(s)):
        #     c=0
        #     for j in range(len(s)):
        #         if s[i]==s[j]:
        #             c=c+1

        #     if c==1:
        #         return i
        # return -1
        # d={}
        # for i in s:
        #     d[i]=d.get(i,0)+1
        # for i in range(len(s)):
        #     if d[s[i]]==1:
        #         return i
        # return -1



