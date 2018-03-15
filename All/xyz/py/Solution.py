#type here
i=str(raw.input())
print (i)
j=str(input())
k=str(input())
l=int(j,16)
m=int(k,16)
if(i is '+'):
    print("1")
    x=int(l+m)
if(i=='-'):
    x=int(l-m)
if(i=='*'):
    x=int(l*m)
if(i=='/'):
    x=int(l/m)