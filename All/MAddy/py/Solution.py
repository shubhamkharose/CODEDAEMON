def addme(n,L,R):
    su=0
    for i in n:
        su+=int(i)
        if su>=L and su<=R:
            return 1
    return 0

n,q,L,R = map(int,raw_input().split())
a = [0]*n
while(q>0):
    s,x,y = map(int,raw_input().split())
    if s == 1:
        a[x-1] = y
    else:
        i=1
        cnt=0
        b= a[x-1:y]
        l=len(b)
        while(i<=l):
            j=0
            while(j+i<=l):
                cnt+=addme(b[j:j+i:],L,R)
                j+=1
            i+=1
        print cnt
    q-=1  