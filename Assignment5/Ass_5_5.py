from MarvellousString import *

accpetString=input("Enter the String : ")
sum,total=addASCIIForString(accpetString)
print("Sum is {}".format(sum))
print("Total chars are {}".format(total))

print("The Average of all Values is: {}".format(int(sum/total)))

# Output
# PS E:\Assignments\Python\Python_Essentials\Assignment5> python .\Ass_5_5.py
# Enter the String : ABCDE
# Char A = ASCII 65.
# Char B = ASCII 66.
# Char C = ASCII 67.
# Char D = ASCII 68.
# Char E = ASCII 69.
# Sum is 335
# Total chars are 5
# The Average of all Values is: 67
