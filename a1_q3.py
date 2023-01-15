t=int(input('enter the no. of numbers to be added:'))
for i in range (t):
    flag=False
    n=int(input('enter the number:'))
    for j in range (2,n):
        if n%j==0:
            flag=True
    if flag==True:
        print('not prime')
    else:
        print('prime')
