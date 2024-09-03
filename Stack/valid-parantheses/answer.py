class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {"}":"{",")":"(","]":"["}
        stack = []
        for c in s:
            if c not in dict:
                stack.append(c)
                continue
            if len(stack) == 0 or stack[len(stack) - 1] != dict[c]:
                return False
            stack.pop()
        return len(stack) == 0

