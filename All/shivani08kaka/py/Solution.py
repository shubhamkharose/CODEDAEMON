n = raw_input() 
n = int(n)
for i in range(0, n):
    word = str(raw_input())
    def palindrome(word):
     for i in range(len(word)//2):
        if word[i] != word[-1-i]:
                 return False
        return True
if not result:
    print 'NO'
else:
    print 'YES