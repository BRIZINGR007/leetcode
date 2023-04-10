# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums) -> int:
        nums.sort()
        dict={}
        i,count=0,0
        while i<len(nums)-1:
            if nums[i]!=nums[i+1]:
                dict[nums[i]]=count
                count=0
                i+=1
            elif nums[i]==nums[i+1]:
                count+=1
                i+=1
            if i== len(nums)-1:
                dict[nums[i]]=count
        if len(nums)==1:
            return nums[0]
        return (max(dict,key=lambda x:dict[x]))