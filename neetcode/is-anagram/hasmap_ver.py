class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)): return False
        
        hashS, hashT = {}, {}

        for i in range(len(s)):
            # .get() to give default value when its init
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        for h in (hashS):
            if hashS[h] != hashT.get(h, 0): return False
        
        return True

        