class Solution:
    def sequence(self, N):
        # code here
        if N == 1:
            return 1
        sol = 1
        last_value = 1
        for i in range(2, N+1):
            last_value += 1
            for x in range(last_value, last_value + i):
                last_value = x
                if i == N:
                    sol *= x
        return sol + self.sequence(N - 1)




solution = Solution()
print(solution.sequence(5))