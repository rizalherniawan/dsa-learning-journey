from collections import deque

class Solution:
    
    #Function to find maximum of each subarray of size k.
   def max_of_subarrays(self,arr,n,k):
        ans = list()
        start = 0
        temp = deque()
        pole = 0
        for i in range(n):
            while len(temp) > 0 and arr[i] > temp[-1]:
                temp.pop()
            temp.append(arr[i])
            pole += 1
            if pole >= k:
                ans.append(temp[0])
                if temp[0] == arr[start]:
                    temp.popleft()
                start += 1
        return ans
        


sol = Solution()
print(sol.max_of_subarrays([1000,5,1,2,3,4,15,12,90,13],10,4))




# steps:
# 1) loop array 
# 2) dalam looping jumlahkan angka penanda
# 3) dalam looping tentukan juga nilai maks dari masing - masing element
# 4) jika angka penanda >= jumlah subarray 
# 5) masukan nilai maks kedalam array
# 6) ubah nilai variable start atau penanda angka awal element dari subarray