#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
char * string(char *a)
{
    char b[100];
    int z;
    int i,k,l;
    l=strlen(a);
    i=0;
    k=0;
    while(i<l)
    {
        if(a[i]==a[i+1])
            i=i+2;
        else
        {
            b[k]=a[i];
            k++;
            i++;
        }
    }
    b[k]='\0';
    if(k==0)
        return '\0';
    else
    {
        if(strcmp(a,b)==0)
            return a;
        else
            a=string(b);
    }
}
int main() 
{
    char * b=(char *)malloc(100*sizeof(char));
    scanf("%s",b);
    b=string(b);
    int i=0,j=strlen(b)-1;
    while(i<j)
    {
        if(b[i++]!=b[j--])
            break;
    }
    if(i<j)
        printf("NO");
    else
        printf("YES");
    return 0;
}