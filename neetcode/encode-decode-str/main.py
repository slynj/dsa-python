# https://neetcode.io/problems/string-encode-and-decode

class Solution:

    def encode(self, strs: List[str]) -> str:
        sentence = ""
        word_length = ""
        sentence_length = 0

        for i in range(len(strs)):
            sentence += strs[i]
            if i != 0:
                word_length += "#"
            word_length += str(len(strs[i]))
            sentence_length += len(strs[i])
        
        return  sentence + word_length + "#" + str(sentence_length)

    def decode(self, s: str) -> List[str]:
        if len(s) == 2:
            return []

        length = ""

        for char in s[::-1]:
            if char != "#":
                length = s[-1] + length
                s = s[:-1]
            else:
                break
        
        sentence = s[:int(length)]
        word_length = s[int(length):-1]
        word_length = word_length.split("#")

        sentence_list = []
        index = 0

        for i in word_length:
            i = int(i)
            sentence_list.append(sentence[:i])
            sentence = sentence[i:]

        return sentence_list



            

