n=int(input('enter the value of n:'))
for i in range (n//2+1):
    print('* '*((n//2)+1-i),'  '*(2*i+1),'* '*((n//2)+1-i))
for j in range (1,n//2+1):
    print('* '*(j+1),'  '*(n-2*j),'* '*(j+1))
