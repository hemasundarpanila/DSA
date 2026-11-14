class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ss=0
        tt=0
        while ss<len(s):
            while tt<len(t):
                if s[ss]==t[tt]:
                    tt=tt+1
                    break
                tt=tt+1
            else:
                return False
            ss=ss+1
        return True





















        # ti=0
        # si=0
        # while(si<len(s)):
        #     while(ti<len(t)):
        #         if s[si]==t[ti]:
        #             ti+=1
        #             break
        #         ti+=1
        #     else:
        #         return False
        #     si+=1
        # return True