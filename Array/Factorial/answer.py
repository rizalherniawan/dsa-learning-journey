class Solution:
    def factorial(self, N):
        #code here
        ans = list()
        total = 1
        for i in range(total, N+1):
            total *= i
        total = str(total)
        for i in range(len(total)):
            ans.append(total[i])
        return ans

    
solution = Solution()
print(solution.factorial(10))