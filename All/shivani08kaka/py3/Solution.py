n = input() 
n = int(n)
for i in range(0, n):
    S = input()
    def isPalindrome(S):
        for i in range(0, len(S)):
            if S[0 + i] == S[len(S) - 1]:
                pass
            else:
                break

if not len(S):
    print('NO')
else:
    print('YES')