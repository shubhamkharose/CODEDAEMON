#include <iostream>
#include <cmath>
#include <string>
#include<cstdio>
using namespace std;
void decToHexa(int n)
{   
    char hexaDeciNum[100];
     
    int i = 0;
    while(n!=0)
    {   
        int temp  = 0;
         
        temp = n % 16;
         
        if(temp < 10)
        {
            hexaDeciNum[i] = temp + 48;
            i++;
        }
        else
        {
            hexaDeciNum[i] = temp + 55;
            i++;
        }
         
        n = n/16;
    }
     
    for(int j=i-1; j>=0; j--)
        cout << hexaDeciNum[j];
}

int main()
{
    char x;
    cin >> x;
    char c1[100], c2[100];
    scanf("%s", c1);
    scanf("%s", c2);
    int n1=0, n2=0;
    for(int i=0; c1[i]!='\n' && c1[i]!=0 ; i++)
    {
            if(c1[i]>='0' && c1[i]<='9')
                n1=n1*16+(c1[i]-'0');
            else if(c1[i]=='A' || c1[i]=='a')
                n1=n1*16+(10);
            else if(c1[i]=='B' || c1[i]=='b')
                n1=n1*16+(11);
            else if(c1[i]=='C' || c1[i]=='c')
                n1=n1*16+(12);
            else if(c1[i]=='D' || c1[i]=='d')
                n1=n1*16+(13);
            else if(c1[i]=='E' || c1[i]=='e')
                n1=n1*16+(14);
            else if(c1[i]=='F' || c1[i]=='f')
                n1=n1*16+(15);
    }
    for(int i=0; c2[i]!='\n' && c2[i]!=0 ; i++)
    {
            if(c2[i]>='0' && c2[i]<='9')
                n2=n2*16+(c2[i]-'0');
            else if(c2[i]=='A' || c2[i]=='a')
                n2=n2*16+(10);
            else if(c2[i]=='B' || c2[i]=='b')
                n2=n2*16+(11);
            else if(c2[i]=='C' || c2[i]=='c')
                n2=n2*16+(12);
            else if(c2[i]=='D' || c2[i]=='d')
                n2=n2*16+(13);
            else if(c2[i]=='E' || c2[i]=='e')
                n2=n2*16+(14);
            else if(c2[i]=='F' || c2[i]=='f')
                n2=n2*16+(15);
    }
    int ans;
    if(x=='+')
    {
      ans = n1+n2;  
    }
    if(x=='*')
    {
      ans = n1*n2;  
    }
    if(x=='-')
    {
      ans = n1-n2;  
    }
    if(x=='/')
    {
      ans = n1/n2;  
    }
    decToHexa(ans);
    return 0;
}
