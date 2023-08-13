def dec2bin(num, n, bi): # (0, 0, "")
    if n == 0:
        return 0
    elif num >= 1:
        return dec2bin(num // 2, n, bi + str(num % 2))
    elif num == 0 and len(bi) < n:
        bi = bi[::-1]
        bi = '0' * (n - len(bi)) + bi[0:]
        return bi
    elif len(bi) == n:
        return bi[::-1]
    
def show_bit(num, inp, bi):
    if inp < 0:
        print("Only Positive & Zero Number ! ! !")
        return
    elif num == (2 ** inp) - 1:
        print(dec2bin(num, inp, bi)) # (0, 0, "")
        return
    elif num < (2 ** inp) - 1:
        bi = dec2bin(num, inp, bi)
        print(bi) # 000
        return show_bit(num + 1, inp, "")

inp = int(input("Enter Number : "))
show_bit(0, inp, "")