# 💡  problem analysis & summary

- Given a sentence consisting of words, reverse each word in the sentence while maintaining the word order in the sentence.

# 💡  algorithm structure

- Split the sentence into individual words using the `split()` method.
- Reverse each word using string slicing `[::-1]`.
- After reversing each word, join the words back into a sentence using `' '.join()` to maintain the word order.

# 💡  code

```python
T = int(input())

for i in range(T):
    sentence = input()
    words = sentence.split()
    reversed_words = []
    
    for word in words:
        reversed_words.append(word[::-1])
    
    reversed_sentence = ' '.join(reversed_words)
    
    print(reversed_sentence)

```

```python
T = int(input())

for i in range(T):
    sentence = input()
    reversed_sentence = ' '.join([word[::-1] for word in sentence.split()])
    print(reversed_sentence)
```

# 💡  time complexity

- `O(T * N)`, where `T` is the number of sentences and `N` is the average length of each sentence.

# 💡  cause of failure

- Wasn’t properly understanding the role of join and split

# 💡  fix & alternative approach

- **Stack for Each Word**:
    - For each word in the sentence, push all characters into a stack.
    - Then, pop characters from the stack to reverse the word.
- **Maintain Word Order**:
    - After reversing each word, maintain the word order by appending each reversed word into a result list.
- **Print the Result**:
    - After processing all the words, join them with spaces and print the final reversed sentence.

```python
T = int(input())

for _ in range(T):
    sentence = input()
    result = []
    
    for word in sentence.split():
        stack = list(word)
        reversed_word = ''
        
        while stack:
            reversed_word += stack.pop()
        
        result.append(reversed_word)
    
    print(' '.join(result))
```

# 💡  take aways & key points

- practice string manip
- time complexity of strin manip