class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        l = 0
        r = len(matrix) - 1
        while l <= r:
            mid = l + ((r - l) // 2)

            if matrix[mid][0] <= target:
                m = matrix[mid]
                li = 0
                ri = len(m) - 1
                while li < ri:
                    mid = li + ((ri - li) // 2)
                    if m[mid] < target:
                        li += 1
                    elif m[mid] > target:
                        ri -= 1
                    else:
                        return True
                l += 1
            
            elif matrix[mid][0] > target:
                r -= 1
            
            else:
                return True

        return False

sol = Solution()

m = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
t = 3


print(sol.searchMatrix(m,t))