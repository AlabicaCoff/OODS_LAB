def bubble(l, sub):
    for last in range(len(l) - 1, 0, -1):
        for i in range(last):
            if sub:
                if l[i] > l[i + 1]:
                    l[i], l[i + 1] = l[i + 1], l[i]
            else:
                if len(l[i]) > len(l[i + 1]):
                    l[i], l[i + 1] = l[i + 1], l[i]
                elif len(l[i]) == len(l[i + 1]):
                    for j in range(0, len(l[i])):
                        if l[i][j] > l[i + 1][j]:
                            l[i], l[i + 1] = l[i + 1], l[i]
                            break
                        elif l[i][j] < l[i + 1][j]:
                            break

def calcSubset(A, res, subset, index, k):
    if sum(subset) == k:
        new_subset = [] + subset
        bubble(new_subset, True)
        res.append(new_subset[:])
    for i in range(index, len(A)):
        subset.append(A[i])
        calcSubset(A, res, subset, i + 1, k)
        subset.pop()
 
def subsets(A, k):
    subset = []
    res = []
    index = 0
    calcSubset(A, res, subset, index, k)
    return res

def print_subset(res):
    if res: 
        for subset in res: print(subset)
    else:
        print("No Subset")
 
result, inp = input("Enter Input : ").split('/')
inp = list(map(int, inp.split()))
res = subsets(inp, int(result))
bubble(res, False)
print_subset(res)