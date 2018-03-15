#include <stdio.h>
#include <string.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        int n,k;
        scanf("%d %d",&n,&k);
        int a[n],zero=0;
        for(int i=0;i<n;i++){
            scanf("%d",&a[i]);
            if(a[i]==0)
                zero+=1;
        }
        if(zero>=k)
            puts("beautiful");
        else
            puts("not beautiful");
    }
       //type your code here
}
