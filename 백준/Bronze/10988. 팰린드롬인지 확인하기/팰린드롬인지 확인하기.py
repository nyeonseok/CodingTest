word = list(map(str, input()))

if word == word[::-1]:
    print("1")
else:
    print("0")


