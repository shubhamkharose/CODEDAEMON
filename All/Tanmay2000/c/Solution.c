#include<stdio.h>
int main()
{
      int no,ne=5,bin=0,base=0,i=0,res;
      no=ne;
      while(ne>0)
      {
          bin=ne%2;         
          if(bin==1)        
          i++;              
          ne=ne/2;          
          res=bin+base*10;   
          base++;           
      }
      printf("%d",res);
      printf("\n The no of 1's are :%d",i);
      
     return 0;
}