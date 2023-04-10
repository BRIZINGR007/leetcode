class Solution:
    def generate(self, numRows):
        list=[[1]]
        for i in range(numRows-1):
            temp=[0]+list[-1]+[0]
            row=[]
            for j in range(len(list[-1])+1):
                row.append(temp[j]+temp[j+1])
            list.append(row)
        return list
ob=Solution()
print(ob.generate(5))
