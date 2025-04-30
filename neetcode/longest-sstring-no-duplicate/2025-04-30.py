class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        sstr = set()
        length = 0

        for r in range(len(s)):
            if s[r] not in sstr:
                sstr.add(s[r])
                length = max(length, r - l + 1)
            else:
                while s[r] in sstr:
                    sstr.remove(s[l])
                    l += 1
                
                sstr.add(s[r])
                length = max(length, r - l + 1)
        
        return length
