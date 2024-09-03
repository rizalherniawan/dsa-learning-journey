import math

nums = [5,7,7,7,7,8,9,10]

def searchRange(nums, target):
    res = [-1,-1]
    if len(nums) == 0:
        return res
    res[0] = searchRightOrLeft(nums, target, True)
    res[1] = searchRightOrLeft(nums, target, False)
    return res

def searchRightOrLeft(nums: list[int], target: int, isSearchingLeft: bool) -> int:
    left, right = 0, len(nums) - 1
    idx = -1
    while left <= right:
        mid = left + (right - left) //2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            idx = mid
            if isSearchingLeft == True:
                right = mid - 1
            else:
                left = mid + 1
    return idx


print(searchRange(nums,12))

        