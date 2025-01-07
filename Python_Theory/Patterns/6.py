#number pyramid2

num = int(input("Enter no. of rows : "))

for i in range(num, 0, -1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()