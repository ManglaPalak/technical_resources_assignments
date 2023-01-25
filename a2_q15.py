n=int(input('enter the value of n:'))
for i in range (1,n//2+2):
    print('  '*((n//2)+1-i),end='')
    for j in range (i,2*i):
        print(j,end=' ')
    for k in range (2*i-2,i-1,-1):
        print(k,end=' ')
    print()
for i in range (n//2,0,-1):
    print('  '*((n//2)+1-i),end='')
    for j in range (i,2*i):
        print(j,end=' ')
    for k in range (2*i-2,i-1,-1):
        print(k,end=' ')
    print()
