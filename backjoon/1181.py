# https://www.acmicpc.net/problem/1181

N = int(input())
words = []
for _ in range(N):
    words.append(input())

words.sort(key=lambda word: (len(word), word))

previous_word = ""
for word in words:
    if previous_word != word:
        print(word)
        previous_word = word
