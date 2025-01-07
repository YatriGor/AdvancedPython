#left pyramid

num = int(input("Enter the no. of rows : "))

for i in range(1, num+1):
    for j in range(i):
        print("*", end='')
    print()