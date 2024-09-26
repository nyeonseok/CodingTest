x, y, w, h = map(int, input().split())

if w//2 < x:
    print(min(w-x, h-y, y))
else:
    print(min(x, h-y, y))
