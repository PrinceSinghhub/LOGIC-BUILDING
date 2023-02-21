n=5
for i in range(n,0,-1):
    for j in range(0,n-i):
        print(" ",end="")
    for j in range(n):
        if i == n:
            print("*", end="")
        elif i == 1:
            print("*", end="")
        elif j == n - 1:
            print("*", end="")
        elif j == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()