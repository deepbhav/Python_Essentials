from functools import *

arr=list()

def acceptList(no):
    for i in range(0,no):
        num=input("Enter {} no : ".format(i+1))
        arr.append(num)
    return arr

no=input("Enter how many Elements do you want :")
arr=acceptList(int(no))

for i in range(2, len(arr)): 
    arr = list(filter(lambda x: int(x) == i or int(x) % i , arr))


for i in range(len(arr)):
    if (arr[i]=='1'):
        arr.remove('1')

afterFilterList=arr
print("After Filter function execution List is : - {} .".format(afterFilterList))
afterMap=list(map(lambda no: int(no) * 2,afterFilterList))

print("After Map function execution List is : - {} .".format(afterMap))

maxx=reduce(max,afterMap)
print("The Max from {} is : {} .".format(afterMap,maxx))


# Output :
# PS E:\Assignments\Python\Assignment4> python .\Ass_4_5.py
# Enter how many Elements do you want :6
# Enter 1 no : 4
# Enter 2 no : 3
# Enter 3 no : 2
# Enter 4 no : 1
# Enter 5 no : 9
# Enter 6 no : 6
# After Filter function execution List is : - ['3', '2'] .
# After Map function execution List is : - [6, 4] .
# The Max from [6, 4] is : 6 .