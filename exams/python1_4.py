print("*** String Rotation ***")
str1, str2 = input("Enter 2 strings : ").split(" ")
temp1, temp2 = str1, str2
Rfirst, Rsecond = "", ""
Lfirst, Lsecond = "", ""
round = 0
while (temp1 != Rsecond + Rfirst) or (temp2 != Lsecond + Lfirst):
    round += 1
    Rfirst = str1[0 : len(str1) - 1]
    Rsecond = str1[len(str1) - 1 : ]
    Lfirst = str2[0]
    Lsecond = str2[1 : ]
    str1 = Rsecond + Rfirst
    str2 = Lsecond + Lfirst
    if round < 6:
        print(f"{round} {str1} {str2}")
    elif round == 6 and (temp1 == str1 and temp2 == str2):
        print(f"{round} {str1} {str2}")
if round > 6:
    print(" . . . . . ")
    print(f"{round} {str1} {str2}")
print(f"Total of  {round} rounds.")