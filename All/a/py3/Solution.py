t=list(input())

a=int(input(),16)
b=int(input(),16)

if t[0]=="+":
    j=hex(a+b)
    print(j[2:])
elif t[0]=="-":
    j=hex(a-b)
    print(j[2:])
elif t[0]=="*":
    j=hex(a*b)
    print(j[2:])

elif t[0]=="%":
    j=hex(a%b)
    print(j[2:])