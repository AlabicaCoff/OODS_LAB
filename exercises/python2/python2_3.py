def mod_position(arr, s):
    mod_list = []
    for i in range(len(arr)):
        if (i + 1) % int(s) == 0:
            mod_list.append(arr[i])
    print(mod_list)

print("*** Mod Position ***")
string, mod = input("Enter Input : ").split(",")
mod_position(string, mod)