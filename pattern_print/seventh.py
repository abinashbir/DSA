row=int(input("Enter the number of row : "))

for i in range(1,row):
    for j in range(1,row-i+1):
            print(" ",end="")
    for k in range(1,2*i):
            print("*",end="")
    print("")
        
    