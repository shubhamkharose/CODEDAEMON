
m=str(input())
print (m)
j=str(input())
k=str(input())
l=int(j,16)
m=int(k,16)
if(m=='+'):
        x=int(l+m)
        print(format(x, '02x'))
if(m=='-'):
        x=int(l-m)
        print(format(x, '02x'))
if(m=='*'):
        x=int(l*m)
        print(format(x, '02x'))
if(m=='/'):
        x=int(l/m)
        print(format(x, '02x'))