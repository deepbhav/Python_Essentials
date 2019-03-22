from MarvellousString import *

accpetString=input("Enter the String : ")
sum,total=addASCIIForString(accpetString)
print("Sum is {}".format(sum))
print("Total chars are {}".format(total))

print("The Average of all Values is: {}".format(int(sum/total)))

