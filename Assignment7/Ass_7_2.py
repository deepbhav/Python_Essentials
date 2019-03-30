class BankAccount:

    ROI=10.5
    def __init__(self):
        name=input("Enter the Name: ")
        amount=input("Enter the Amount: ")
        self.Name=name
        self.Amount=float(amount)
        self.Interest=0.0

    def Deposite(self):
        depo_Amt=input("Enter Amout to be deposited: ")
        self.Amount=self.Amount+float(depo_Amt)
        
    def Withdraw(self):
        withdraw_Amt=input("Enter Amout to be withdrawal: ")
        self.Amount=self.Amount-float(withdraw_Amt)

    def CalculateInterest(self):
        no_Of_Days=input("Enter no of Days: ")
        self.Interest=float((float(no_Of_Days)*self.Amount*BankAccount.ROI)/100)
        print("Interest is : ",self.Interest)
    
    def Display(self):
        print("Account Holder Name : ",self.Name)
        print("Account Balance is : ",self.Amount)

print("\nAfter creating the First Object")
# First Object Creation
obj=BankAccount()
obj.Display()
obj.Deposite()
obj.Display()
obj.Withdraw()
obj.Display()
obj.CalculateInterest()

print("\nAfter creating the Second Object")
# Second Object Creation
obj1=BankAccount()
obj1.Display()
obj1.Deposite()
obj1.Display()
obj1.Withdraw()
obj1.Display()
obj1.CalculateInterest()

# Output
# PS I:\Assignments\Assignment-9> python .\Ass_7_2.py

# After creating the First Object
# Enter the Name: Deepak
# Enter the Amount: 1500
# Account Holder Name :  Deepak
# Account Balance is :  1500.0
# Enter Amout to be deposited: 0
# Account Holder Name :  Deepak
# Account Balance is :  1500.0
# Enter Amout to be withdrawal: 0
# Account Holder Name :  Deepak
# Account Balance is :  1500.0
# Enter no of Days: 15
# Interest is :  2362.5

# After creating the Second Object
# Enter the Name: Suraj
# Enter the Amount: 500
# Account Holder Name :  Suraj
# Account Balance is :  500.0
# Enter Amout to be deposited: 0
# Account Holder Name :  Suraj
# Account Balance is :  500.0
# Enter Amout to be withdrawal: 0
# Account Holder Name :  Suraj
# Account Balance is :  500.0
# Enter no of Days: 3
# Interest is :  157.5