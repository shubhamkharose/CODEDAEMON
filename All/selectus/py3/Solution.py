t=int(input())

for i in range(t):
    a=input()
    x=list()
    y=0
    b=a.split(" ")
    s=int(b[0])
    
    for j in range(s+1):
        k=j
        y=int(y)+int(len(x)+1)
        
        x.clear()
        while(k>=0):
            r=k%int(b[-1])
            k=int(k/int(b[-1]))
            x.append(r)
    print(y-1)