#question 554. Brick_wall_leetcode
wall = [[1],[1],[1]]
hash={0:0}
for array in wall:
    x=0
    for j in range(len(array)-1):
        x=x+array[j]
        hash[x] = hash.get(x,0)+1
print(len(wall)-max(hash.values()))
