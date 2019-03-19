# 5.Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().

arr = list()
cnt = 0


def acceptNumbers(no):
    for i in range(no):
        num = input("Enter {} th no : ".format(i+1))
        arr.append(int(num))
    return arr
