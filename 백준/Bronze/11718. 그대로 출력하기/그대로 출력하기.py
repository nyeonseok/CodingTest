while True:
    try:
        input_list = list(input())
        for i in input_list:
            print(i, end='')
    except EOFError:
        break
    print()
