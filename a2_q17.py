n=int(input('enter the value for n:'))
for i in range (1,n//2+1):
    print(' '*(n//2+1),'* '*i)
print('* '*n)
for j in range (n//2,0,-1):
    print(' '*(n//2+1),'* '*j)
