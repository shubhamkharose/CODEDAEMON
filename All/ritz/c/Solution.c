#include <stdio.h>
#include <string.h>
int main()
{
       char opr;
       scanf("%c",&opr);
       int a,b;
       scanf("%x%x",&a,&b);
       int res;
       if(opr=='+')
           res = a+b;
       else if(opr == '-')
           res = a-b;
       else if(opr == '*')
            res = a*b;
        else
            res = a%b;
    printf("%x",res);
            
}
