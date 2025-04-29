class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l, r = 0, 0
        sstr = {}
        while r < len(s):
            sstr[s[r]] = 1 + sstr.get(s[r], 0)

            if (r - l + 1) - max(sstr.values()) <= k:
                res = max(res, r - l + 1)
                r += 1

            else:
                sstr[s[l]] -= 1
                sstr[s[r]] -= 1

                l += 1
      
        return res
            

