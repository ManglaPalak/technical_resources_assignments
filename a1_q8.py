num=int(input('enter the number:'))
k=int(input('enter the number of times n to be rotated:'))
n=str(num)
num1=num
if k>0:
    for i in range (k):
        r=0
        rem=num1%10
        r=rem*(10**(len(n)-1))+num1//10
        num1=r
    print('rotate:',num1)
l=n.split()
if k<0:
    for j in range (k):
         x=l.pop(0)
         l.append(x)
print('rotate:',end='')
for i in l:
    print(i,end='')
