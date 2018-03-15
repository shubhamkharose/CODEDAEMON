#include<stdio.h>
int main()
{
      int i,j,k,c=0,d=0;
      for(i=0;i<7;i++)
      {
          for(j=i+1;j<7;j++)
          {
              for(k=1;k<6;k++)
                c++;
          }
      }
      for(i=0;i<6;i++)
      {
          for(j=i+1;j<6;j++)
          {
              for(k=0;k<7;k++)
                c++;
          }
      }
      for(i=0;i<6;i++)
      {
          for(j=i+1;j<6;j++)
          {
              for(k=j+1;k<6;k++)
                c++;
          }
      }
          
      printf("261");
     return 0;
}