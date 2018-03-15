#include <bits/stdc++.h>


int main()
{
    int t;
    int tot=0;
    scanf("%d",&t);
  //  printf("alan");
    for(int i=0;i<t;i++)
    {
        tot=0;
        int a,b;
        int l=1;
        scanf("%d %d",&a,&b);
        for(int j=0;j<=a;j++)
        {
            if(j>=pow(b,l))
            {
                l++;
             //   j--;
           }
            tot=tot+l;
        }
        printf("%d\n",tot);
    }
	//type here
}