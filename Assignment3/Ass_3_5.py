# 5.Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
from MarvellousNum import *
from functools import *

arr = list()
primeList = list()


def acceptNumbers(no):
    for i in range(no):
        num = input("Enter {} th no : ".format(i+1))
        arr.append(int(num))
    return arr


def primeListFun(no):
    for i in range(no):
        if(primeCheck(arr[i]) == True):
            if(arr[i] == 1):
                continue
            else:
                primeList.append(arr[i])
    return primeList


no = input("Enter how many no you want to insert:")
acceptNumbers(int(no))
print("List Contains : ", arr)
primeList = primeListFun(int(no))
print("Prime List Contains : ", primeList)

print("Addition of {0} is :{1}.".format(primeList,
                                        reduce((lambda no1, no2: no1+no2), primeList)))


# Output
# PS C:\add_Project\Assignment3> python .\Ass_3_5.py
# Enter how many no you want to insert:5
# Enter 1 th no : 15
# Enter 2 th no : 45
# Enter 3 th no : 3
# Enter 4 th no : 11
# Enter 5 th no : 39
# List Contains :  [15, 45, 3, 11, 39]
# Prime List Contains :  [3, 11]
# Addition of [3, 11] is :14.
