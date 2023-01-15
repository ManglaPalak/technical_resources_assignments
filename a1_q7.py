n=int(input('enter a number:'))
inv=0
op=1
while n!=0:
    od=n%10
    id=op
    ip=od
    inv=inv+id*int((10**(ip-1)))
    n=n/10
print('inverse:',inv)
