def display_pattern(no):
    for i in range(0,no):
        print("*",end='\t',flush=True)
no=input("Enter no:- ")
display_pattern(int(no))