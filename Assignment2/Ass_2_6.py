def pf_pattern(no):
    for i in range(0, no):
        for j in range(no, i, -1):
            print("*", end='\t', flush=True)
        print("\n")


n = input("Enter number: ")
pf_pattern(int(n))
