def odd_list(al):
    odds = []
    for num in al:
        if num % 2 != 0:
            odds.append(num)
    return odds


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)