n=5
num1=0
num2=1
print('0')
print('1',end=' ')
for i in range (n):
    for j in range (i+1):
        print(num1+num2,end=' ')
        temp=num1
        num1=num2
        num2=num2+temp
    print()
