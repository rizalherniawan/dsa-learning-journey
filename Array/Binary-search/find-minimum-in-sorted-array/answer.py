
def findMin(nums: list[int]) -> int:
    l = 0
    r = len(nums) - 1
    res = float('inf')
    while l <= r:
        mid = l + (r - l) // 2
        res = min(res, nums[mid])
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid - 1
    return res

print(findMin([9,10,1,2,3,5,7]))
