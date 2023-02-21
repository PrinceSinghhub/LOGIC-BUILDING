n=int(input())
for i in range(n):

    for j in range(i,n):
        print(" ",end="")

    for j in range(n):
        if i ==0:
            print("*", end="")
        elif i == n-1:
            print("*", end="")
        elif j==n-1:
            print("*", end="")
        elif j==0:
            print("*", end="")
        else:
            print(" ",end="")
    print()