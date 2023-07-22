permute_col = []
print("*** Fun with permute ***")
num_list= [int(n) for n in input("input : ").split(",")]
print(f"Original Cofllection:  {num_list}")
print("Collection of distinct numbers:")

if len(num_list) == 0:
    print("[]")
if len(num_list) == 1:
    print(num_list)

result = [[]]
for i in num_list:
    temp_list = []
    for j in result:
        for k in range(len(j) + 1):
            temp_list.append(j[:k] + [i] + j[k:])
            result = temp_list
            print(result)
print(f" {result}")