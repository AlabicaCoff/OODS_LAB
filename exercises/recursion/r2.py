data = input("Enter your List : ").split(",")
data = list(map(int, data))

def order_list(l, ind):
    if ind > len(l) - 1:
        return 0
    elif ind == len(l) - 1:
        return l
    elif l[ind + 1] > l[0]:
        great = l.pop(ind + 1)
        l.insert(0, great)
    elif l[ind + 1] > l[ind]:
        great = l.pop(ind + 1)
        l.insert(ind, great)
        return order_list(l, ind - 1)
    return order_list(l, ind + 1)

print(f"List after Sorted : {order_list(data, 0)}")