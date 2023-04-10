class HelloMoto:
    def searchRange(self,nums,target):
        left=self.bin_Search_left(nums,target)
        right=self.bin_Search_right(nums,target)
        return [right,left]
    def bin_Search_left(self,nums, target):
        if target>nums[len(nums)-1]:
            return -1
        if target<nums[0]:
            return -1
        l,r=0,len(nums)-1
        i=-1
        while l<=r:
            m=(l+r)//2
            z=nums[m]
            if target>nums[m]:
                l=m+1
            elif target<nums[m]:
                r=m-1
            else:
                i=m
                r=m-1
                """if left_Bias:
                    r=m-1
                else:
                    l=m+1"""
        return i
    
    def bin_Search_right(self,nums, target):
        if target>nums[len(nums)-1]:
            return -1
        if target<nums[0]:
            return -1
        l,r=0,len(nums)-1
        i=-1
        while l<=r:
            m=(l+r)//2
            z=nums[m]
            if target>nums[m]:
                l=m+1
            elif target<nums[m]:
                r=m-1
            else:
                i=m
                l=m+1
                """if left_Bias:
                    r=m-1
                else:
                    l=m+1"""
        return i
z=HelloMoto()
print(z.searchRange(nums = [5,7,7,8,8,10], target = 7))


