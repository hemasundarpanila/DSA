class Solution:
    # def validPalindrome(self, s: str) -> bool:
    #     class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l=l+1
                r=r-1
            return True
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return check(l+1,r) or check(l,r-1)
            l=l+1
            r=r-1
        return True
















        # def check(l, r):
        #     while l < r:
        #         if s[l] != s[r]:
        #             return False
        #         l += 1
        #         r -= 1
        #     return True
        # l, r = 0, len(s) - 1
        # while l < r:
        #     if s[l] != s[r]:
        #         return check(l + 1, r) or check(l, r - 1)
        #     l += 1
        #     r -= 1
        # return True
        # l=0
        # r=len(s)-1
        # b=False
        # while l<r:
        #     if s[l]==s[r]:
        #         l=l+1
        #         r=r-1
        #     elif s[l]!=s[r]:
        #         l=l+1
        #     else:
        #         return False
        # return True

            
                
        