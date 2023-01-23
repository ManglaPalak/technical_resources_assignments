n=int(input('enter value of n:'))
for i in range (1,(n//2)+2):
    for j in range (1,i+1):
        print(j,end=' ')
    print(' '*(n-2*i-1),end='')
    for k in range (i,0,-1):
        if k==i:
            print(' '*(n-2*i),k,end='')
        else:
            print(k,end=' ')
    print()
