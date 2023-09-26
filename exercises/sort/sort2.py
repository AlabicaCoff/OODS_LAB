def selection(l):
    for last in range(len(l) - 1, 0, -1):
        if l[last] < 0:
            pass
        else:
            big_i = 0
            big = l[big_i]
            for i in range(1, last + 1):
                if l[i] > big:
                    big = l[i]
                    big_i = i
            l[last], l[big_i] = l[big_i], l[last]

inp = list(map(int, input("Enter Input : ").split()))
selection(inp)
print(' '.join(list(map(str, inp))))