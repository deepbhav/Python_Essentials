from MarvellousString import *

accpetString=input("Enter the String : ")
pos=input("Enter the Position")
print("String before removing char from pos {} is {}: ".format(pos,accpetString))
s=deleteByPosition(accpetString,int(pos))
print("String after removing char from pos {} is {}: ".format(pos,s))

# Output
# PS E:\Assignments\Python\Python_Essentials\Assignment5> python .\Ass_5_4.py
# Enter the String : Deepak
# Enter the Position4
# String before removing char from pos 4 is Deepak:
# String after removing char from pos 4 is Deeak: