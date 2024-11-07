# https://neetcode.io/problems/anagram-groups

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list_h = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                i = ord(c) - ord('a')
                count[i] += 1
            
            list_h[tuple(count)].append(s)
        
        return list(list_h.values())


        