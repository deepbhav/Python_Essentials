# 4.Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.

arr = list()
cnt = 0


def acceptNumbers(no):
    for i in range(no):
        num = input("Enter {} th no : ".format(i+1))
        arr.append(int(num))
    return arr


def findFrequency(arr, key):
    global cnt
    for i in range(len(arr)):
        if(arr[i] == key):
            cnt = cnt+1
    return cnt


no = input("Enter how many no do you want :")
arr = acceptNumbers(int(no))
print(arr)

key = input("Enter no for which you want to find frequency: ")
cnt = findFrequency(arr, int(key))
print("Frequency of {} in {} is : {} ".format(key, arr, cnt))

# Output :
# PS C:\add_Project\Assignment3> python .\Ass_3_4.py
# Enter how many no do you want :5
# Enter 1 th no : 12
# Enter 2 th no : 56
# Enter 3 th no : 23
# Enter 4 th no : 34
# Enter 5 th no : 12
# [12, 56, 23, 34, 12]
# Enter no for which you want to find frequency: 12
# Frequency of 12 in [12, 56, 23, 34, 12] is : 2
