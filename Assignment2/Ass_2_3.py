def factorial(no):
    fact = 1
    for i in range(1, no+1):
        fact = fact * i
    return fact


no = input("Enter no:")
print(factorial(int(no)))
