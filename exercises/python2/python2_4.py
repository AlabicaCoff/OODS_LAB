numbers = [int(n) for n in input("Enter Your List : ").split()]
expected_list = []
cnt = 0

if len(numbers) < 3:
    print("Array Input Length Must More Than 2")
else:
    for a in range(len(numbers)):
        for b in range(a+1, len(numbers)):
            for c in range(b+1, len(numbers)):
                temp_list = []
                if numbers[a]+numbers[b]+numbers[c] == 0 and numbers[a] != 0 and numbers[b] != 0 and numbers[c] != 0:
                    temp_list.extend([numbers[a], numbers[b], numbers[c]])
                    expected_list.append(temp_list)
                elif numbers[a] == 0 and numbers[b] == 0 and numbers[c] == 0 and cnt == 0:
                    temp_list.extend([numbers[a], numbers[b], numbers[c]])
                    expected_list.append(temp_list)
                    cnt += 1
    print(expected_list)