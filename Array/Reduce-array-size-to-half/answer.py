class Solution:
    def minSetSize(self, arr) -> int:
        mid = len(arr) / 2
        obj = {}
        ans = 1
        for i in range(len(arr)):
            if arr[i] in obj:
                obj[arr[i]] += 1
            else:
                obj[arr[i]] = 1
        freqs = list(obj.values())
        freqs.sort(reverse = True)
        temp_freqs = freqs[0]
        if len(freqs) == 1 or temp_freqs >= mid:
            return ans
        else:
            print(freqs)
            for i in range(len(freqs)):
                temp_freqs += freqs[i+1]
                ans += 1
                if temp_freqs >= mid:
                    print(temp_freqs)
                    break
        return ans

sol = Solution()
sol.minSetSize([1,2,3,4,5,6,7,8,9,10])
            

                    