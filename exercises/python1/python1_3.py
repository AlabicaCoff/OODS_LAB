permute_col = []
print("*** Fun with permute ***")
num_list= [int(n) for n in input("input : ").split(",")]
print(f"Original Cofllection: {num_list}")
print("Collection of distinct numbers:")

if len(num_list) >= 1:
    for a in reversed(range(len(num_list))):
        if len(num_list) >= 2:
            for b in reversed(range(len(num_list))):
                if len(num_list) >= 3:
                    for c in reversed(range(len(num_list))):
                        if len(num_list) >= 4:
                            for d in reversed(range(len(num_list))):
                                if num_list[a] is not num_list[b] and num_list[a] is not num_list[c] and num_list[b] is not num_list[c]:
                                    temp_list1 = [num_list[a], num_list[b], num_list[c]]
                                    permute_col.append(temp_list1)
                        else:
                            if num_list[a] is not num_list[b] and num_list[a] is not num_list[c] and num_list[b] is not num_list[c]:
                                temp_list2 = [num_list[a], num_list[b], num_list[c]]
                                permute_col.append(temp_list2)

print(f" {permute_col}")
