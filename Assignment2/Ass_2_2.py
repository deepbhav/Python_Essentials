def display_star(no):
    for i in range(0, no):
        for j in range(0, no):
            print('*', end='\t', flush=True)
        print("\n")


n = input("Enter how many Times you want to print the Sequence: ")
display_star(int(n))
