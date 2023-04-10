from ast import Return


class Solution:
    def maxProfit(self,z):
        left=0
        right=1
        max_profit=0
        while right<len(z):
            current_profit=z[right]-z[left]
            if z[left]<z[right]:
                max_profit=max(current_profit,max_profit)
            else:
                left= right
            right+=1
        return max_profit

z=[7,1,5,3,6,4]
x=Solution()
print(x.maxProfit(z))