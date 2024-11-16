# https://neetcode.io/problems/longest-substring-without-duplicates

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charS = set()
        l = 0
        lenS = 0

        for r in range(len(s)):
            while s[r] in charS:
                charS.remove(s[l])
                l += 1
            charS.add(s[r])
            lenS = max(lenS, r - l + 1)
        
        return lenS