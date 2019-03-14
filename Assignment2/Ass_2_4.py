def find_factors(no):
    factor = 0
    for i in range(1, no+1):
        if no % i == 0:
            print(i, end='\t', flush=True)
            factor = factor + i
    return factor


n = input("Enter no")
print(find_factors(int(n)))
