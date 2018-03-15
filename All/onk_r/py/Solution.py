t= int(raw_input())
i=1
while(True):
    if(t%i==0):
        no=t/i;
        le=bin(no)[2::]
        if(len(le)%2==0):
            i+=1
            continue
        else:
            l = len(le)/2
            s = '1'*(l+1)
            s +='0'*l
            if le == s:
                print no
                break
    i+=1