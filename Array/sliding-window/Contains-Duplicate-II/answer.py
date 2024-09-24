def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    my_dict = {}
    for i in range(len(nums)):
        if nums[i] in my_dict:
            temp = abs(my_dict[nums[i]] - i)
            if temp <= k:
                return True
        my_dict[nums[i]] = i
    return False