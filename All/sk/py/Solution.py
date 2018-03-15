s = raw_input()
s = s[::-1]
k = int(raw_input())
i = 0
su = 0
ans = ''
carry = 0
while ( i < len(s)):
    digits = s[i:i+k:]
    c=carry
    for _ in digits:
        c+=int(_)
    #print c,carry
    if(c>=10):
        carry = c/10
        
    else:
        carry = 0
    if c >= 10:
        ans =  str(c/10) + ans 
    else:
        ans = str(c) +ans 
    #print 'ans',ans
    i+=k
print ans

