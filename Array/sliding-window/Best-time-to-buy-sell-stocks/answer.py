from collections import deque

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        temp = deque()
        for i in range(len(prices)):
            temp.append(prices[i])
            if len(temp) == 2:
                if temp[0] < temp[-1]:
                    ans = min(ans, temp[0] - temp[-1])
                    temp.pop()
                else:
                    temp.popleft()  
        return abs(ans)

sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))
        