print(" *** Rank score ***")
rank_dict = {}
input_list = [num for num in input("Enter ID and Score end with ID : ").split()]
id = input_list.pop()
print(input_list)
print(id)
for i in range(len(input_list)):
    if i % 2 == 0:
        rank_dict[input_list[i]] = float(input_list[i+1])

sorted_key_dict = {}
sorted_val_dict = {}
sorted_keys = sorted([int(key) for key in rank_dict.keys()], reverse=False)

for w in sorted_keys:
    sorted_key_dict[str(w)] = rank_dict[str(w)]

sorted_val_dict = {k: v for k, v in sorted(sorted_key_dict.items(), key=lambda item: item[1], reverse=True)}
print(sorted_val_dict)
if id in rank_dict.keys():
    print(list(sorted_val_dict.keys()).index(id) + 1)
else:
    print("Not Found")
    
