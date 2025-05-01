class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        length = 0
        sstr = {}

        for r in range(len(s)):
            sstr[s[r]] = 1 + sstr.get(s[r], 0)
            maxchar = max(sstr.values())

            while (r - l + 1) - maxchar > k:
                sstr[s[l]] -= 1
                l += 1
            
            length = max(r - l + 1, length)
        
        return length

