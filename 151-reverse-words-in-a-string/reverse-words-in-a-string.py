class Solution:
    def reverseWords(self, s: str) -> str:
        # left=0
        # right=len(s)-1
        a=[]
        k=s[::-1]
        r=k.split()
        for i in r:
            f=i[::-1]
            a.append(f)
        return " ".join(a)
