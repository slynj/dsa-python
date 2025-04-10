class Solution:
    def isValid(self, s: str) -> bool:
        bracket = []
        bracketPair = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for c in s:
            if c in bracketPair:
                if bracket and bracket[-1] == bracketPair[c]:
                    bracket.pop()
                else:
                    return False
            else:
                bracket.append(c)
                

        return True if not bracket else False

