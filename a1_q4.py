l=int(input('enter the lower limit:'))
u=int(input('enter the upper limit:'))
for i in range (l,u+1):
    flag=False
    for j in range (2,i):
        if i%j==0:
            flag=True
    if flag==True:
        pass
    else:
        print(i,end=',')
