#include <stdio.h>
#include <string.h>
int main()
{   

      int l ,d,f,cnt=0;
       scanf("%d %d %d", &f ,&l, &d);
       int i=l;
        for(i=l;i<=f;i+5)
        {
            cnt++;
        }
        printf("%d",cnt);
        return 0;

}
