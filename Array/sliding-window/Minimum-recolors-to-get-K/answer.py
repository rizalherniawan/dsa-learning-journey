class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = k
        start = 0
        w = 0
        count = 0
        for i in range (len(blocks)):
            if blocks[i] == "W":
                w += 1
            count += 1
            if count == k:
                ans = min(ans,w)
                if blocks[start] == "W":
                    w -= 1
                count -= 1
                start += 1
        return ans


sol = Solution()
sol.minimumRecolors("WBBWWWWBBWWBBBBWWBBWWBBBWWBBBWWWBWBWW",)