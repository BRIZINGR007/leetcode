array=[[1,2,3],[4,5,6],[7,8,9]]
l,r=0,len(array)-1
while l<r:
    for i in range(r-1):
        top,bottom=l,r
        top_left=array[top][l+i]
        array[top][l+i]=array[bottom-i][l]
        array[bottom-i][l]=array[bottom][r-i]
        array[bottom][r-i]=array[top+i][r]
        array[top+i][r]=top_left
    l+=1
    r-=1
print(array)