from collections import deque

class Solution:
    def smallestSubstring(self, S):
        # Code here
        ans = 1E9
        temp = deque()
        count = 0
        for i in range(len(S)):
            temp.append(S[i])
            count += 1
            if len(temp) >= 2:
                if S[i] == temp[0]:
                    if len(temp) == 2:
                        temp.popleft()
                        count -= 1
                    else:
                        while len(temp) != 2:
                            temp.popleft()
                            count -= 1
                if len(temp) > 2 and S[i-1] != temp[-1]:
                    ans = min(ans, count)
                    if ans == 3:
                        return ans
                    while len(temp) != 2:
                        temp.popleft()
                        count -= 1
        if ans < 1E9:
            return ans
        return -1

sol = Solution()
# print(sol.smallestSubstring("120"))
print(sol.smallestSubstring("111121100200001"))