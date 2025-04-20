class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words, count = {}, {}
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for a in alphabet:
            count[a] = 1 + count.get(a, 0)

        for s in strs:
            countS = count.copy()
            
            for c in s:
                countS[c] += 1

            countV = ""
            for key, val in countS.items():
                countV += str(val)
            
            words[countV] = words.get(countV, [])
            words[countV].append(s)
        
        res = []

        for key, val in words.items():
            res.append(val)

        return res

