def display_name(message,no):
    for i in range(0,no):
        print(message)

def check_no(no):
    if(no < 1):
        print("Please enter Integers only.")
    else:
        print("It is okay to go.")
def check_msg(message):
    if(type(message) == "<class 'int'>"):
        print("Please enter String only.")

msg=input("Enter Message you want to print:")
num=input("how many times you want to print:")
check_no(int(num))

display_name(msg,int(num))