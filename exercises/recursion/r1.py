data = input("Enter Input : ").split(" ")
data = list(map(int, data))

def find_max(num, max, ind):
    if num > max:
        max = num
    if num == data[-1]:
        return max 
    return find_max(data[ind + 1], max, ind + 1)

print(f"Max : {find_max(data[0], data[1], 0)}")