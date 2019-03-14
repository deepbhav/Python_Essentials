def pf_pattern(no):
    for i in range(1, no+1):
        for j in range(1, no+1):
            print(j, end='\t', flush=True)
        print("\n")


pf_pattern(5)
