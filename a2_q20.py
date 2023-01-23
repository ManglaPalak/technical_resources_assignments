n=5
for i in range (n//2):
    print('* ','  '*(n-2),' *')
for j in range (1,(n//2)+1):
    if j==1:
        print('*',' '*(n//2),'* ',' '*(n//2),'*')
    else:
        print('*',' '*((n//2)-j),'*',' '*(j-1),'*',' '*(j-1), '*')
print('* ','  '*(n-2),' *')
