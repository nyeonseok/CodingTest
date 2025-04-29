import sys


def score(result):
    score = [0] * len(result)
    for i in range(len(result)):
        if result[i] == "X":
            score[i] = 0
            continue
        else:
            for j in range(i, -1, -1):
                if result[j] == "X":
                    break
                if result[j] == "O":
                    score[i] += 1
    return score


n = int(sys.stdin.readline())
for _ in range(n):
    ox = sys.stdin.readline().strip()
    print(sum(score(ox)))
