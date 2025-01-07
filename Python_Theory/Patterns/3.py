# left no. pyramid

num = int(input("Enter no. of rows: "))

for i in range(1, num+1):
    for j in range(i):
        print(i, end='')
    print()