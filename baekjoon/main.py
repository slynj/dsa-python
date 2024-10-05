T = int(input())

for i in range(T):
    sentence = input()
    reversed_sentence = ' '.join([word[::-1] for word in sentence.split()])
    print(reversed_sentence)
