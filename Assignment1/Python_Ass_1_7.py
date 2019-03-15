def divisible_by_5(no):
    if(no%5==0):
        return True
    else:
        return False

num=input("Enter the no: ")
print(divisible_by_5(int(num)))

