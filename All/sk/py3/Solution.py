a=input()
k=int(input())
a=list(map(int,list(a)))
t=[]
carry=0
for i in range(1,len(a)+1,k):
    if(i<=len(a)-k):
        s=sum(a[-i:-(i+k):-1])
    else:
        s=sum(a[-i::-1])
    if(len(a)-k>=i):
        t.append((s+carry)%10)
    else:
        t.append((s+carry))
    carry=s//10
print(*t[::-1],sep="")
    
    