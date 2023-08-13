# Chapter : 2 - item : 2 - Spherical
# สร้าง class Spherical โดยต้อง
# มี function [changeR , findVolume , findArea]
# มี ตัวแปร radius

# class Spherical:
#     def __init__(self,r):
#         ### Enter Your Code Here ###

#     def changeR(self,Radius):
#         ### Enter Your Code Here ###

#     def findVolume(self):
#         ### Enter Your Code Here ###

#     def findArea(self):
#         ### Enter Your Code Here ###

#     def __str__(self):
#         ### Enter Your Code Here ###

# r1, r2 = input("Enter R : ").split()
# R1 = Spherical(int(r1))
# print(type(R1))
# print(dir(R1))
# print(R1)
# R1.changeR(int(r2))
# print(R1)

class Spherical:
    pi = 3.1415926535897932384626433832795028841
    def __init__(self,radius):
        self.radius = radius

    def changeR(self,Radius):
        self.radius = Radius

    def findVolume(self):
        return 4 / 3 * Spherical.pi * self.radius ** 3

    def findArea(self):
        return 4 * Spherical.pi * self.radius ** 2

    def __str__(self):
        return f"Radius ={self.radius} Volumn = {self.findVolume()} Area = {self.findArea()}"

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)