class Solution:
    def maxArea(self, height: list[int]) -> int:
        max=float("-inf")
        left=0
        right=len(height)-1
        while left<right:
            min_hight=min(height[left],height[right])
            width=right-left
            area=min_hight*width
            if area>max:
                max=area
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max


























        