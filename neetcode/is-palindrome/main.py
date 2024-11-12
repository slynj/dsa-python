# https://neetcode.io/problems/is-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        for c in s:
            if not (c.isalnum()): s = s.replace(c,'')

        index = len(s) - 1

        for i in range(0, len(s)//2):
            if s[i] != s[index-i]: 
                return False
        return True