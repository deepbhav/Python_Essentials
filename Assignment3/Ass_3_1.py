# 1.Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.


def acceptNumbers(no):
    for i in range(0, int(no)):
        num = input("Enter {} no :".format(i))
        arr.append(int(num))
    return arr


no = input("Enter How many no do you want :")
arr = list()
print(acceptNumbers(no))

# Output :
# PS C:\add_Project\Assignment3> python .\Ass_3_1.py
# Enter How many no do you want :5
# Enter 0 no :7
# Enter 1 no :2
# Enter 2 no :7
# Enter 3 no :3
# Enter 4 no :2
# [7, 2, 7, 3, 2]
