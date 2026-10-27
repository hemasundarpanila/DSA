class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            d[s[i]]=d.get(s[i],0)+1
            d[t[i]]=d.get(t[i],0)-1
        for i in d.values():
            if i!=0:
                return False
        return True









        # if len(s)!=len(t):
        #     return False
        # d={}
        # for i in range(len(s)):
        #     d[s[i]]=d.get(s[i],0)+1
        #     d[t[i]]=d.get(t[i],0)-1
        # for i in d.values():
        #     if i!=0:
        #         return False
        # return True

        # d1={}
        # d2={}
        # for i in s:
        #     d1[i]=d1.get(i,0)+1
        # for j in t:
        #     d2[j]=d2.get(j,0)+1
        # if d1==d2:
        #     return True
        # return False
