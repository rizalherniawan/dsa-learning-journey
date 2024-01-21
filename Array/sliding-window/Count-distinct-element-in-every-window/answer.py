class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        ans = list()
        temp = dict()
        count = 0
        start = 0
        for i in range(N):
            count += 1
            if A[i] in temp:
                temp[A[i]] += 1
            else:
                temp[A[i]] = 1
            if count >= K:
                ans.append(len(temp))
                if temp[A[start]] == 1:
                    del temp[A[start]]
                else:
                    temp[A[start]] -= 1
                start += 1
        return ans
    
sol = Solution()
print(sol.countDistinct([1,2,1,3,4,2,3], 7, 4))