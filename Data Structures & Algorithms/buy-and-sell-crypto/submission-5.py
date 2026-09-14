class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p=0
        l=prices[0]
        for i in range(len(prices)):
            l=min(l,prices[i])
            p=max(p,prices[i]-l)
        return p
        # #profit = max(p[i]-p[j])
        # #left<right. ->left+ ?????
        # #left>right. ->left+
        # #right+?
        # l=0
        # r=len(prices)-1
        # p=0
        # while l<r:
        #     print(l,r)
        #     if prices[l]<=prices[r]:
        #         p=max(p,prices[r]-prices[l])
        #         if l<r-1 and l+1<r and prices[r-1]-prices[l]>prices[r]-prices[l+1]:
        #             r-=1
        #         else:
        #             l+=1
        #     else:
        #         if l<r-1 and l+1<r and prices[r-1]>prices[r]:
        #             r-=1
        #         else:
        #             l+=1

        # return p