# https://neetcode.io/problems/longest-repeating-substring-with-replacement

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        maxS = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxCount = max(count.values())

            if (r - l + 1) - maxCount <= k:
                maxS = r - l + 1
            else:
                count[s[l]] -= 1
                l += 1
                
        return maxS