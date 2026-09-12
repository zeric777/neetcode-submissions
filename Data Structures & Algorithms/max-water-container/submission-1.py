class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        m=min(heights[l],heights[r])*(r-l)
        # print(m)
        while l<r:
            if heights[l]>heights[r]:
                r=r-1
            else:
                l=l+1
                
            m=max(min(heights[l],heights[r])*(r-l),m)
        return m
                