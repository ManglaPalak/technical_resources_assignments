n=int(input('enter a number:'))
r=0
for i in range (len(str(n))):
    rem=n%10
    r=r*10+rem
    n=n//10
print('reverse of the number:',r)
