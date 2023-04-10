height=[1,8,6,2,5,4,8,3,7]
l=0
r=len(height)-1
left_max=height[l]
right_max=height[r]
water_level=0
while l<r:
    if left_max>right_max:
        water_level=max(min(left_max,right_max)*(r-l),water_level)
        r-=1
        right_max=max(right_max,height[r])
        
    else:
        water_level=max(min(left_max,right_max)*(r-l),water_level)
        l+=1
        left_max=max(left_max,height[l])    
print(water_level)