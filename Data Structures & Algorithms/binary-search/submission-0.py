class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=set(nums)
        if target in n:
            return nums.index(target)
        else:
            return -1