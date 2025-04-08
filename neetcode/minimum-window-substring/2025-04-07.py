class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "":
            return ""
        
        string = {}
        substr = {}

        for c in t:
            substr[c] = 1 + substr.get(c, 0)

        need = len(substr.keys())
        have = 0

        l, r = 0, 0

        index, minLen = [-1, -1], float("infinity")

        print(substr)

        for i in range(len(s)):
            r = i
            c = s[i]
            string[c] = 1 + string.get(c, 0)

            if c in substr and string[c] == substr[c]:
                have += 1
            
            while have == need:
                if (r - l) + 1 < minLen:
                    index = [l, r]
                    minLen = (r - l) + 1

                string[s[l]] -= 1

                if s[l] in substr and string[s[l]] < substr[s[l]]:
                    have -= 1
                
                l += 1

    

        l = index[0]
        r = index[1]

        return s[l : r + 1] if minLen != float("infinity") else ""
                






