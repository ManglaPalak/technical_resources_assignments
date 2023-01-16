n=int(input('enter a number:'))
for i in range (1,(n//2)+1):
    print(' '*((n//2)-i),'* '*i)
print('* '*((n//2)+1))
for j in range ((n//2),0,-1):
    print(' '*((n//2)-j),'* '*j)
