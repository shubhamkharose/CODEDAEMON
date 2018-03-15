#include <stdio.h>
#include<string.h>
#include<stdlib.h>
int main()
{
	char *a,*b,*c,*ans;
	int i=0,j=0,k=0,l,p;
	a=(char *)malloc(sizeof(char)*51200);
	b=(char *)malloc(sizeof(char)*51200);
	c=(char *)malloc(sizeof(char)*51200);
    scanf("%s",a);
	l=strlen(a);
	while(i<l)
	{
	    if(i%2)
	        b[j++]=a[i];
	    else
	        c[k++]=a[i];
	   i++;
	}
	while(c[p]!='\0')
	{
	    printf("%c",c[p]);
	    p++;
	}
	p=0;
	while(b[p]!='\0')
	{
	    printf("%c",b[p]);
	    p++;
	}
	
}