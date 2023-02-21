n = 100
Num = 1
command = True
for i in range(n):

    NonRev = []
    Rev = []

    if command == True:
        for i in range(5):
            NonRev.append(Num)
            Num += 1

        for i in NonRev:
            print(i, end=" ")
        print()
        NonRev.clear()
        command = False

    else:
        for j in range(5):
            Rev.append(Num)
            Num += 1

        for i in range(len(Rev) - 1, -1, -1):
            print(Rev[i], end=" ")
        print()
        Rev.clear()
        command = True