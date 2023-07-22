print(" *** String count ***")
mes = input("Enter message : ")
ups_cnt = 0
lows_cnt = 0
ups = []
lows = []
for ch in mes:
    if ch.isupper():
        ups_cnt += 1
        if ch not in ups:
            ups.append(ch)
    elif ch.islower():
        lows_cnt += 1
        if ch not in lows:
            lows.append(ch)
ups.sort()
lows.sort()
print(f"No. of Upper case characters : {ups_cnt}")
print("Unique Upper case characters :", end = " ")
for up in ups:
    print(up, end = "  ")
print(f"\nNo. of Lower case Characters : {lows_cnt}")
print(f"Unique Lower case characters :", end = " ")
for low in lows:
    print(low, end = "  ")