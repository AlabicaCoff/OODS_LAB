def bubble(l):
    for last in range(len(l) - 1, 0, -1):
        for i in range(last):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                

inp = list(map(int, input("Enter Input : ").split()))
bubble(inp)
print(inp)