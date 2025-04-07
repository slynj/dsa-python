class Solution:

    def encode(self, strs: List[str]) -> str:
        wlen = ""
        sentence = ""

        for i in range(len(strs)):
            wlen += str(len(strs[i]))

            if i == len(strs) - 1:
                wlen += "#"
            else:
                wlen += ","
            
            sentence += strs[i]

        return wlen + sentence

    def decode(self, s: str) -> List[str]:
        if len(s) < 1 :
            return []
        
        wlen = ""
        lens = []
        res = []
        
        for i in range(len(s)):
            if s[i] != "#":
                wlen += s[i]
            else:
                s = s[i+1:]
                break
        
        lens = wlen.split(",")

        for l in lens:
            l = int(l)
            res.append(s[:l])
            s = s[l:]
        
        return res

            

