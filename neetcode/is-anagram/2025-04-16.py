class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sHash = {}
        tHash = {}

        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                sChar = s[i]
                tChar = t[i]

                sHash[sChar] = 1 + sHash.get(sChar, 0)
                tHash[tChar] = 1 + tHash.get(tChar, 0)
        
        return sHash == tHash

        
