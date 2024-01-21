class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r = len(nums) - 1
        l = 0

        while l <= r:

            mid = l + ((r - l) // 2)

            if nums[mid] > target:

                r -= 1
            
            elif nums[mid] < target:

                l += 1
            
            else:

                return mid
        
        return -1