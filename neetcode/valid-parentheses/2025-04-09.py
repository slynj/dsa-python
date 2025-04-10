class Solution:
    def isValid(self, s: str) -> bool:
        bracket = []
        bracketPair = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in range(len(s)):
            if s[i] in bracketPair.values():
                bracket.append(s[i])
            else:
                if bracket and bracket[-1] == bracketPair[s[i]]:
                    bracket = bracket[:len(bracket) - 1]
                    length -= 2

        return length == 0

