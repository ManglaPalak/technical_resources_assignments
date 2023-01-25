n=int(input('enter the value of n:'))
print('  '*(n//2+1),' * ')
for i in range (n//2):
    print('  '*((n//2)-i),'* ','  '*(2*i+1),'* ')
for j in range (1,n//2):
    print('  '*(j+1),'* ','  '*j,'* ')
print('  '*(n//2+1),' * ')
