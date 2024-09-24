from collections import deque

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        my_set = set()
        max_val = 0
        start_index = 0
        for i in range(len(s)):
            while s[i] in my_set:
                my_set.remove(s[start_index])
                start_index += 1
            my_set.add(s[i])
            max_val = max(max_val, i - start_index + 1)
        return max_val
    

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcabcdefgh"))