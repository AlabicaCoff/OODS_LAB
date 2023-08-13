# Chapter : 2 - item : 3 - Mod Position
# ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการแสดงตำแหน่งของ List ในตำแหน่งที่หารเลขใดๆลงตัว จาก String

# def mod_position(arr, s):
#     //Code Here

# Input ตำแหน่งที่แรกเป็นค่าใน String ที่นำเข้ามา

# Input ตำแหน่งที่สองเป็นตัวเลขที่ทำการบอกว่าจะแสดงที่ตำแหน่งที่หารตัวเลขนั้นๆลงตัว เช่นถ้าใส่เลข 3 และ String มีค่าเป็น ABCDEFG ก็จะแสดงตำแหน่งที่ 3 คือ C กับตำแหน่งที่ 6 คือ F 

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