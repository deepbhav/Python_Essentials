# 3.Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.


arr = list()
min = 100000000000000000000


def acceptNumbers(no):
    for i in range(no):
        num = input("Enter {} th no : ".format(i+1))
        arr.append(int(num))
    return arr


def findMin(arr):
    for i in range(len(arr)):
        global min
        if(arr[i] < min):
            min = arr[i]
    return min


no = input("Enter how many no do you want :")
arr = acceptNumbers(int(no))
print(arr)

maxNum = findMin(arr)
print("The Minimum no in Entered numbers is  :", maxNum)
