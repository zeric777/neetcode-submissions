class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # r=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if -(nums[i]+nums[j]) in nums[j+1:]:
        #             l=[nums[i],nums[j],-(nums[i]+nums[j])]
        #             l.sort()
        #             if l not in r:
        #                 r.append(l)  
        # return r
        re=[]
        nums.sort()
        for i,e in enumerate(nums):
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]>-e:
                    r=r-1
                elif nums[l]+nums[r]<-e:
                    l=l+1
                else:
                    if [e,nums[l],nums[r]] not in re:
                        re.append([e,nums[l],nums[r]])
                    l += 1
                    r -= 1
        return re
            
        
        