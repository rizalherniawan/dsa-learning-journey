def removeElement(nums, val: int):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    print(arr)
    return k

arr = [0,2,2,5,7,2,6,2]
print(removeElement(arr,2))

            