
def removeDuplicates(nums: list[int]) -> int:
        L = 1
        
        for R in range(1, len(nums)):
            if nums[R] != nums[R - 1]:
                nums[L] = nums[R]
                L += 1
        print(nums)
        return L
    

nums = [0,0,1,1,1,2,2,3,3,4]
print(len(nums))
print(removeDuplicates(nums))