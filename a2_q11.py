n=int(input('enter the value of n:'))
num=1
for i in range (n):
    for j in range (i+1):
        print(num,end=' ')
        num=num+1
    print()
