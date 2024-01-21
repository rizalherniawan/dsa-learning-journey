class Solution:
    def findSpecialInteger(self, arr) -> int:
        unique_number = set(arr)
        count = 0
        total = 0
        ans = 0
        for i in range(len(arr)):
            if arr[i] in unique_number:
                count += 1
            if total < count:
                total = count
                ans = arr[i]
            if i + 1 < len(arr):
                if arr[i] != arr[i+1]:
                    count = 0
        return ans


solution = Solution()
arr = [1,1,1,1,1,1,2,3,4,5,6,7,8,9,10,11,12,12,12,12]
print(solution.findSpecialInteger(arr))