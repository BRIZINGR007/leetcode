s = "dvdf"
res=""
count=0
for i in s:
    if i not in res:
        res+=i
    else:
        res = res[res.index(i) + 1:] + i
    count=max(count,len(res))
print(count)