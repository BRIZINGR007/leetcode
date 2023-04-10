height=[0,1,0,2,1,0,1,3,2,1,2,1]
max_left=[0]*len(height)
for x in range(1,len(height)):
    max_left[x]=max(height[x-1],max_left[x-1])

max_right=[0]*len(height)
for x in range(len(height)-2,-1,-1):
    max_right[x]=max(max_right[x+1],height[x+1])
res=0
for x in range(len(height)):
    water_level=min(max_right[x],max_left[x])
    if water_level>=height[x]:
        res+=water_level-height[x]
print(res)

#o(N) space complexity
height=[1,8,6,2,5,4,8,3,7]
l,r=0,len(height)-1
left_max=height[l]
right_max=height[r]
res=[]
while l<r:
    if left_max<right_max:
        l+=1
        left_max=max(left_max,height[l])
        res.append(left_max-height[l])
    else:
        r-=1
        right_max=max(right_max,height[r])
        res.append(right_max-height[r])
print(res)
