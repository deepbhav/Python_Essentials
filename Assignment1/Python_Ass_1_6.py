def checkNo(no):
    if(no == 0):
        print("No is Zero.")
    elif(no > 0 ):
        print("No is Positive.")
    else:
        print("No is Negative")

num=input("Enter Number: ")
checkNo(int(num))