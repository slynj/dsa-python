class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "": return ""

        index, minLen = [-1, -1], float("infinity")
        string, substr = {}, {}

        for char in t:
            substr[char] = 1 + substr.get(char, 0)
        
        need = len(substr.keys())
        have = 0

        l = 0
        
        for i in range(len(s)):
            char = s[i]
            r = i
            string[char] = 1 + string.get(char, 0)

            if (char in substr) and (string[char] == substr[char]):
                have += 1
            
            while have == need:
                if (r - l + 1) < minLen:
                    minLen = r - l + 1
                    index = [l, r]
                
                string[s[l]] -= 1
                
                if s[l] in substr and string[s[l]] < substr[s[l]]:
                    have -= 1
                
                l += 1
            
            r += 1

        l, r = index
        return s[l : r + 1] if minLen != float("infinity") else ""






