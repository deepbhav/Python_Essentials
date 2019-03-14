# import Arithmetic as a
from Arithmetic import *

no1 = input("Enter First no: ")
no2 = input("Enter Second no: ")

ans = Add(int(no1), int(no2))
print("The Addition is :")
print(ans)

ans = Sub(int(no1), int(no2))
print("The Subtraction is :")
print(ans)

ans = Mult(int(no1), int(no2))
print("The Multiplication is :")
print(ans)

ans = Div(int(no1), int(no2))
print("The Division is :")
print(ans)
