n = int(input())

print(2**n - 1)


def hanoi(n, start, mid, end):
    if n == 1:
        print(f"{start} {end}")
        return
    hanoi(n - 1, start, end, mid)
    print(f"{start} {end}")
    hanoi(n - 1, mid, start, end)


hanoi(n, 1, 2, 3)
