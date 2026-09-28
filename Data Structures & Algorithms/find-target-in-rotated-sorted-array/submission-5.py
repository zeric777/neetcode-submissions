class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            if nums[0]==target:
                return 0
            else:
                return -1
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            print(nums[l],nums[m],nums[r],l,m,r)
            if nums[m]==target:
                return m
            elif nums[l]==target:
                return l
            elif nums[r]==target:
                return r

            if nums[m]>=nums[l]:
                if nums[m]<target or nums[l]>target:
                    l=m+1
                else:
                    r=m
            else:
                if nums[m]>target or nums[r]<target:
                    r=m
                else:
                    l=m+1
        return -1
