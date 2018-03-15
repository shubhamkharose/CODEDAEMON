#include <stdio.h>
#include <string.h>
#include<math.h>

int power(int a,int b)
{
    int sum=0;
    while(b)
    {
        sum+=a;
    }
    return sum;
    
}
#include <stdio.h>
#include <string.h>
#include<math.h>
int hex(char * hex)
{
     int decimal, place;
    int i = 0, val, len,p;
      len = strlen(hex);
    len--;

    /*
     * Iterate over each hex digit
     */
    for(i=0; hex[i]!='\0'; i++)
    {

        /* Find the decimal representation of hex[i] */
        if(hex[i]>='0' && hex[i]<='9')
        {
            val = hex[i] - 48;
        }
        else if(hex[i]>='a' && hex[i]<='f')
        {
            val = hex[i] - 97 + 10;
        }
        else if(hex[i]>='A' && hex[i]<='F')
        {
            val = hex[i] - 65 + 10;
        }
        p= power(16,len);
        decimal += val *p;
        len--;
    }
    return decimal;
}
int main()
{
     char c;
     char a[100],b[100];
     printf("emnasjdk");
     scanf("%c %s %s",&c,a,b);
     int f=hex(a);
     int g=hex(b);
     printf("%d %d",f,g);

}
