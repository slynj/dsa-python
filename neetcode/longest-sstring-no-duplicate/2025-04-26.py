class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        length = 0
        maxLength = 0
        setS = set()

        for c in s:
            if c not in setS:
                setS.add(c)
                length += 1
            else:
                maxLength = max(maxLength, length)
                length = 1
                setS = set()
                setS.add(c)

        maxLength = max(maxLength, length)
        
        return maxLength
            



