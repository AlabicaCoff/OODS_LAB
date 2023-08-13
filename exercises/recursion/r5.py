def asteroid_collision(asts ,ind):
    if ind >= len(asts) - 1 or asts == []:
        return asts
    elif (asts[ind + 1] > 0 and asts[ind] < 0) or (asts[ind + 1] < 0 and asts[ind] > 0):
        if abs(asts[ind + 1]) > abs(asts[ind]):
            asts.pop(ind)
            return asteroid_collision(asts, ind - 1)
        elif abs(asts[ind + 1]) < abs(asts[ind]):
            asts.pop(ind + 1)
            return asteroid_collision(asts, ind - 1)
        elif abs(asts[ind + 1]) == abs(asts[ind]):
            asts.pop(ind)
            asts.pop(ind)
            return asteroid_collision(asts, ind - 2)
    return asteroid_collision(asts, ind + 1) 

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x, 0))