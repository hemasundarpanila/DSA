class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=len(s)-1
        l=0
        while(l<r):
            if s[l].isalnum() and s[r].isalnum():
                le=s[l].lower()
                re=s[r].lower()
                if le!=re:
                    return False
                l=l+1
                r=r-1
            elif not s[l].isalnum():
                l=l+1
            else:
                r=r-1
        else:
            return True
            














        # l=0
        # r=len(s)-1
        # while(l<r):
        #     if s[l].isalnum() and s[r].isalnum():
        #         le=s[l].lower()
        #         re=s[r].lower()
        #         if le!=re:
        #             return False
        #             break
                
        #         l=l+1
        #         r=r-1
        #     elif s[l].isalnum():
        #         r=r-1
        #     elif s[r].isalnum():
        #         l=l+1
        #     else:
        #         l=l+1
        #         r=r-1
        # else:
        #     return True

        