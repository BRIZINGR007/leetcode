class Solution:
    def sortColors(self, nums):
        if len(nums) <=1:
            return nums
        mid = len(nums)//2
        left=nums[:mid]
        right=nums[mid:]
        self.sortColors(left)
        self.sortColors(right)
        self.merge_two_sorted_array(nums,left,right)
        return nums

    def merge_two_sorted_array(self,array,left,right):
        len_l=len(left)
        right_l=len(right)
        i=j=k=0
        while i<len_l and j<right_l:
            if left[i]<right[j]:
                array[k] = left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
            k+=1
        
        
        while i<len_l:
            array[k]=left[i]
            i+=1
            k+=1
        while j<right_l:
            array[k]=right[j]
            j+=1
            k+=1
sort = Solution()
print(sort.sortColors(nums = [2,0,2,1,1,0]))