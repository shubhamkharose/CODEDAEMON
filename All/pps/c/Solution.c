#include <stdio.h>
#include <stdlib.h>
//using namespace std;
int main()
{
       //type your code here
       int t;
       int n, k, flg;;
       for (int i=0;i <t; i++)
       {
           scanf ("%d%d", &n, &k);
           int a [n];
           for (int j=0; j <n; j++)
           {
               scanf ("%d", &a [j]);
           }
           for (int j=0;j <n; j++)
           {
               if (a [j]==0)
               flg=1;
               else
           {
               flg=0;break;
           }
           }
           if (flg==1)
           printf("beautiful");
           else
           printf ("not beautiful");
       }
}

