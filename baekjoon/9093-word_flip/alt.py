# using stack data structure

T = int(input())

for i in range(T):
    sentence = input()
    result = []

    for word in sentence.split():
        stack = list(word) 
        reversed_word = ''
        
        while stack:
            reversed_word += stack.pop()
        
        result.append(reversed_word)
    
    print(' '.join(result))