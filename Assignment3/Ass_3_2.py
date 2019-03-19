# 2. Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.

arr = list()
max = -1


def acceptNumbers(no):
    for i in range(no):
        num = input("Enter {} th no : ".format(i+1))
        arr.append(int(num))
    return arr


def findMax(arr):
    for i in range(len(arr)):
        global max
        if(arr[i] > max):
            max = arr[i]
    return max


no = input("Enter how many no do you want :")
arr = acceptNumbers(int(no))
print(arr)

maxNum = findMax(arr)
print("The Maximum no in Entered numbers is  :", maxNum)

# Output :
# PS C: \add_Project\Assignment3 > python .\Ass_3_2.py
# Enter how many no do you want: 5
# Enter 1 th no: 34
# Enter 2 th no: 90
# Enter 3 th no: 233
# Enter 4 th no: 0
# Enter 5 th no: 56
# [34, 90, 233, 0, 56]
# The Maximum no in Entered numbers is: 233
