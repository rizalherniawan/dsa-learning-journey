import math

def minEatingSpeed(piles, h):
    piles.sort()
    left = 1
    right = piles[len(piles) - 1]
    res = right
    while left <= right:
        mid = left + (right - left) // 2
        temp_sum = 0
        for i in range(0, len(piles)):
            if mid > piles[i]:
                temp_sum += 1
            else:
                temp = math.ceil(piles[i] / mid)
                temp_sum += temp
        if temp_sum > h:
            left = mid + 1
        else:
            res = mid
            right = mid - 1
    return res

print(minEatingSpeed([312884470],312884469))



        