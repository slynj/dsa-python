class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return 1 if len(s) == 1 else 0
        
        l, r = 0, 1
        maxL = 1
        sstr = {}
        sstr[s[l]] = 1 + sstr.get(s[l], 0)

        while l <= r and r < len(s):
            sstr[s[r]] = 1 + sstr.get(s[r], 0)
            while sstr[s[r]] > 1 and l <= r:
                sstr[s[l]] -= 1
                l += 1

            maxL = max(maxL, r - l + 1)
            r += 1

        
        return maxL




        

