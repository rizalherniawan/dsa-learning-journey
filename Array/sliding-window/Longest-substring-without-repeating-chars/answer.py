from collections import deque

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = dict()
        temp = deque()
        count = 0
        ans = 0

        if len(set(s)) == len(s):
            ans = len(s)
            return ans

        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] += 1
            else:
                map[s[i]] = 1

            if map[s[i]] > 1:
                # count -= 1
                # if s[i] != s[i-1]:
                #     count += 1
                ans = max(ans, count)
                while temp[0] != s[i]:
                    if map[temp[0]] > 1:
                        map[temp[0]] -= 1
                    else:
                        del map[temp[0]]
                    temp.popleft()
                    count -= 1
                if temp[0] == s[i]:
                    map[temp[0]] -= 1
                    temp.popleft()
                    count -= 1
                temp.append(s[i])
                count += 1
                # # map[s[i]] = 1
                # temp.append(s[i])
                # # count = 2

            else:
                temp.append(s[i])
                count += 1
                if i == len(s) - 1:
                    ans = max(ans,count)
        return ans
    

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcabcdefgh"))