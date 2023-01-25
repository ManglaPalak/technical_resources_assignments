n=int(input('enter the value of n:'))
print('* '*n)
for i in range (1,n//2):
    print('  '*i,'* ','  '*((n//2+1)-i),'* ')
for j in range (n//2+1):
    print('  '*((n//2)-j),'* '*(2*j+1))
