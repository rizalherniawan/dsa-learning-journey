
def countEleLessThanOrEqual(arr1,n1,arr2,n2):
    #returns the required output
    arr2.sort()
    ans = []
    for i in range (0, len(arr1)):
        low = 0
        high = n2 - 1
        res = 0
        while low <= high:
            mid = low + (high - low) // 2
            if arr1[i] >= arr2[mid]:
                low = mid + 1
                res = low
            else:
                high = mid - 1
        ans.append(res)
    return ans


arr1 = [1,2,3,4,7,9,0]
arr2 = [1,1,2,1,1,4]
print(countEleLessThanOrEqual(arr1,len(arr1),arr2,len(arr2)))