import math

def sqrtx(x: int) -> int:
    if x == 0 or x == 1:
        return x
    high = x 
    low = 1
    while low <= high:
        mid = low + (high - low) // 2
        if mid*mid == x or (mid*mid < x and (mid+1)*(mid+1) > x):
            return mid
        elif mid*mid > x:
            high = mid - 1
        else:
            low = mid + 1

print(sqrtx(2))