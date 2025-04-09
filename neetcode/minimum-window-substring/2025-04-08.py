class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == "": return ""

        string = {}
        substr = {}
        index, minLen = [-1, -1], float("infinity")
        
        for c in t:
            substr[c] = 1 + substr.get(c, 0)
        
        l = 0
        need = len(substr.keys())
        have = 0

        for r in range(len(s)):
            c = s[r]
            string[c] = 1 + string.get(c, 0)

            if c in substr and string[c] == substr[c]:
                have += 1

                while need == have:
                    if (r - l) + 1 < minLen:
                        index = [l, r]
                        minLen = (r - l) + 1

                    string[s[l]] -= 1

                    if s[l] in substr and string[s[l]] < substr[s[l]]:
                        have -= 1

                    l += 1
        
        l, r = index
        if minLen < float("infinity"):
            return s[l : r + 1]
        else:
            return ""
