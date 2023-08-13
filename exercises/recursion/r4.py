def pantip(k, n, arr, path, patt):
    print(f"n : {n}, path : {path}, patt : {patt}")
    if n > len(arr) - 1:
        return len(d.keys())
    elif patt + str(n) in d.keys():
        print(f"patt + str(n) : {patt + str(n)}, dict_key : {d.keys()}")
        return pantip(k, n + 1, arr, path, patt)
    elif sum(path) + arr[n] == k:
        path.append(arr[n])
        d[patt + str(n)] = path
        print(f"path : {path}, dict_key : {d}")
        print(' '.join(list(map(str, path))))
        return pantip(k, 0, arr, [], "")
    elif sum(path) + arr[n] < k:
        path.append(arr[n])
        print(f"path : {path}")
        return pantip(k, n + 1, arr, path, patt + str(n))
    return pantip(k, n + 1, arr, path, patt)

d = {}
inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [], "")
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))