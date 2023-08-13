# Chapter : 2 - item : 3 - Mod Position
# ให้นักศึกษาเขียนโปรแกรมภาษา Python โดยใช้ Function ในการแสดงตำแหน่งของ List ในตำแหน่งที่หารเลขใดๆลงตัว จาก String

# def mod_position(arr, s):
#     //Code Here

# Input ตำแหน่งที่แรกเป็นค่าใน String ที่นำเข้ามา
# Input ตำแหน่งที่สองเป็นตัวเลขที่ทำการบอกว่าจะแสดงที่ตำแหน่งที่หารตัวเลขนั้นๆลงตัว เช่นถ้าใส่เลข 3 และ String มีค่าเป็น ABCDEFG ก็จะแสดงตำแหน่งที่ 3 คือ C กับตำแหน่งที่ 6 คือ F 

def mod_position(arr, s):
    mod_list = []
    for i in range(len(arr)):
        if (i + 1) % int(s) == 0: # pos of element are divible by input
            mod_list.append(arr[i])
    print(mod_list)

print("*** Mod Position ***")
string, mod = input("Enter Input : ").split(",")
mod_position(string, mod)