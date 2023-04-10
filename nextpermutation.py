class Solution:
    def nextPermutation(self, nums):
        size=len(nums)
        slast=size-2
        while slast>=0 and nums[slast]>=nums[slast+1]:
            slast-=1
        if slast==-1:
            return nums.reverse()
        for x in range(size-1,slast,-1):
            if nums[slast]<nums[x]:
                nums[slast],nums[x]=nums[x],nums[slast]
                break
        nums[slast+1:]=sorted(nums[slast+1:])
        return nums

ans=Solution()
array=[1,3,2]
print(ans.nextPermutation(array))