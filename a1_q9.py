num1=int(input('enter the first number:'))
num2=int(input('enter the second number:'))
div=[]
mul=[]
for i in range (1,max(num1,num2)):
    if num1%i==0 and num2%i==0:
        div.append(i)
print('Greatest Common Divisor is:',max(div))
for j in range (1,num1*num2):
    if j%num1==0 and j%num2==0:
        mul.append(j)
print('Lowest Common Multiple is:',min(mul))
