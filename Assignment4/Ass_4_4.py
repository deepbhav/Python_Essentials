from functools import *

arr=list()

def acceptList(no):
    for i in range(0,no):
        num=input("Enter {} no : ".format(i+1))
        arr.append(num)
    return arr

no=input("Enter how many Elements do you want :")
arr=acceptList(int(no))
print("The Accepted List from user is {} ".format(arr))


evenList=list(filter(lambda no: ( int(no)%2 == 0),arr))

print("After applying Filter function the list is {} ".format(evenList))

squareList=list(map(lambda no: int(no) * int(no),evenList))

print("After applying Map function the list is {} ".format(squareList))

additionOfAll=reduce(lambda no1,no2 : int(no1)+(no2),squareList)

print("Addtion of all Even Sqaures {} is : {}.".format(squareList,additionOfAll))

# Output
# PS E:\Assignments\Python\Assignment4> python .\Ass_4_4_1.py
# Enter how many Elements do you want :5
# Enter 1 no : 33
# Enter 2 no : 44
# Enter 3 no : 88
# Enter 4 no : 44
# Enter 5 no : 44
# The Accepted List from user is ['33', '44', '88', '44', '44']
# After applying Filter function the list is ['44', '88', '44', '44']
# After applying Map function the list is [1936, 7744, 1936, 1936]
# Addtion of all Even Sqaures [1936, 7744, 1936, 1936] is : 13552.