nums = [1,1,1,2,2,3]
k = 2
hash_map={}
freq=[[] for i in range(len(nums)+1)]
for n in nums:
    hash_map[n]=1+hash_map.get(n,0)
for n,c in hash_map.items():
    freq[c].append(n)
print(freq)
res=[]
for i in range(len(freq)-1,0,-1):
    for n in freq[i]:
        res.append(n)
    if len(res)==k:
        print(res)

