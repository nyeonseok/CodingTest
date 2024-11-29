import sys

a, b = map(int, sys.stdin.readline().strip().split())

words = dict()

for _ in range(a):
    word = sys.stdin.readline().strip()
    if len(word) < b:
        continue
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

words = dict(sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))

for k, v in words.items():
    print(k)
