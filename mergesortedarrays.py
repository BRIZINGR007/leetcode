nums1 = [4,5,6,0,0,0]
nums2 = [1,2,3]
m=len(nums1)-len(nums2)
n=len(nums2)
last1=m+n-1
while m>0 and n>0:
    if nums1[m-1]>nums2[n-1]:
        nums1[last1]=nums1[m-1]
        m-=1
    else:#nums1[m]>nums2[n]
        nums1[last1]=nums2[n-1]
        n-=1
    last1-=1
while n>0:
    nums1[last1]=nums2[n-1]
    n-=1
    last1-=1
print(nums1)