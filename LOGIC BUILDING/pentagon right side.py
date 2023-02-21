n=5
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(n):
        print("*",end="")

    print()