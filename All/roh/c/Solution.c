#include <stdio.h>
#include <string.h>
int main()
{int t,i,n,j,l,k,flg=0;
    scanf("%d",&t)  ;
    scanf("%d %d",&n,&k);
    int a[n],b[k];
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
        
    }
    for(i=0;i<n;i++)
    {
        if(a[i]==0)
        {
            for(j=0;j<k;j++)
            {
            b[j]=a[i];
        }
            }
        else 
        {
        printf("not beautiful");
        return 0;
        }
    }
     printf("beautiful");
    
return 0;
}