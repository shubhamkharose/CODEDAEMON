t=int(input())
for i in range(t):
    k=[]
    a,b,c=map(int,input().split())
    k.append(int(((a**2+b**2-2*(c//2)**2)//2)**.5))
    k.append(int(((b**2+c**2-2*(a//2)**2)//2)**.5))
    k.append(int(((c**2+a**2-2*(b//2)**2)//2)**.5))
    print(*k,sep=" ")
    
