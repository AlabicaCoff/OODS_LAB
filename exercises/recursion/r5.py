def asteroid_collision(asts ,ind):
    if ind <= 0:
        return asts
    elif ind >= len(asts):
        pass
    elif asts[ind - 1] > 0 and asts[ind] < 0:
        if abs(asts[ind - 1]) > abs(asts[ind]):
            asts.pop(ind)
            return asteroid_collision(asts, ind)
        elif abs(asts[ind - 1]) < abs(asts[ind]):
            asts.pop(ind - 1)
        elif abs(asts[ind - 1]) == abs(asts[ind]):
            asts.pop(ind)
            asts.pop(ind - 1)
    return asteroid_collision(asts, ind - 1)

x = input("Enter Input : ").split(",")
x = list(map(int, x))
print(asteroid_collision(x, len(x) - 1))