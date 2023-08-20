def pantip(k, n, arr, path, patt): # Using dict to keep the pattern as a key and to keep the path as a value for the amount of patterns
    # print(f"n : {n}, path : {path}")
    if path == [] and n == len(arr) - 1: # If path is empty and n is the last index of arr
        if arr[n] == k:
            d[patt + ' ' + str(n)] = [arr[n]]
            print(arr[n]) 
        return len(d.keys()) # return length of dict keys list for patterns
    elif n > len(arr) - 1: # If n is greater than last index of arr, then pop the last element of path and recall function with new parameter
        path.pop()
        patt_list = patt.split(' ')
        return pantip(k, int(patt_list.pop()) + 1, arr, path, ' '.join(patt_list)) # New parameter n = index of pop element, remove the last patt number
    elif sum(path) + arr[n] == k: # If sum of path + current product price == money, keep in dict and print path then recall function with parameter n + 1
        d[patt + ' ' + str(n)] = path
        print(f"{' '.join(list(map(str,path)))} {arr[n]}" if path != [] else arr[n])
        return pantip(k, n + 1, arr, path, patt)
    elif sum(path) + arr[n] < k: # If sum of path + current product price < money then recall function with parameter n + 1
        return pantip(k, n + 1, arr, path + [arr[n]], patt + ' ' + str(n))
    else:
        return pantip(k, n + 1, arr, path, patt) # Moreover the above conditions, just recall function with parameter n + 1

d = {}
inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]), 0, arr, [], "")
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], pattern))