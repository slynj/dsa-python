# O(T * n)

T = int(input())

# O(T)
for i in range(T):
    sentence = input()
    # O(n), n is the length of the sentence
    reversed_sentence = ' '.join([word[::-1] for word in sentence.split()])
    print(reversed_sentence)
