class MyInt():
    def __init__(self, num):
        self.num = num
    
    def isPrime(self):
        if self.num > 1:
            for i in range(2, self.num):
                if (self.num % i) == 0:
                    return False
            return True
        else:
            return False
        
    def showPrime(self):
        prime_list = []
        if self.num > 1:
            for i in range(self.num + 1):
                if MyInt(i).isPrime():
                    prime_list.append(i)
            print(*prime_list)
        else:
            print("!!!A prime number is a natural number greater than 1")

    def __sub__(self, other):
        return self.num - int(other.num / 2)
    
print(" *** class MyInt ***")
input1, input2 = input("Enter 2 number : ").split(" ")
num1 = int(input1)
num2 = int(input2)
print(f"{num1} isPrime : {MyInt(num1).isPrime()}")
print(f"{num2} isPrime : {MyInt(num2).isPrime()}")
print(f"Prime number between 2 and {num1} :", end = " ")
MyInt(num1).showPrime()
print(f"Prime number between 2 and {num2} :", end = " ")
MyInt(num2).showPrime()
print(f"{num1} - {num2} =", end = " ")
print(MyInt(num1) - MyInt(num2))
