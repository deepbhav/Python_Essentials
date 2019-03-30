class BookStore:
    NofoBooks=0

    def __init__(self):
        name=input("Enter name: ")
        author=input("Enter Author: ")
        self.Name=name
        self.Author=author
        BookStore.NofoBooks=BookStore.NofoBooks+1

    def Display(self):
        print("Name",end="\t\t",flush=True)
        print("Author",end="\t\t",flush=True)
        print("NofoBooks",end="\t\t",flush=True)
        print("\n")
        print(self.Name,end="\t",flush=True)
        print(self.Author,end="\t",flush=True)
        print(BookStore.NofoBooks,end="\t",flush=True)
        print("\n#######################################################3\n")


obj=BookStore()
obj.Display()

obj1=BookStore()
obj1.Display()


# Output
# PS I:\Assignments\Assignment-9> python .\Ass_7_1.py
# Enter name: Wings of Fire
# Enter Author: APJ Kalam
# Name            Author          NofoBooks

# Wings of Fire   APJ Kalam       1
# #######################################################3

# Enter name: Mrutunjay
# Enter Author: Dont know
# Name            Author          NofoBooks

# Mrutunjay       Dont know       2
# #######################################################3