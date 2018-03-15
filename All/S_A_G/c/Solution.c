#include<stdio.h>
#include<string.h>
#include<stdlib.h>
//using namespace std;
int main()
{
	char *s=(char *)malloc(1000*sizeof(char));
	
	char *d1=(char *)malloc(1000*sizeof(char));
	
	char *d2=(char *)malloc(1000*sizeof(char));
	int i,j=0,m=0;
	scanf("%s",s);
	int l=strlen(s);
	for(i=0;i<l;i++)
	{
	  if(s[i]==32)
	  {
	      i++;
	      continue;
	  }
	    if(s[i]>=97 && s[i]<=122)
	    {
	        d2[m++]=s[i];
	    }
	    else
	    {
	    char ch=(char)(s[i]-48);
	    if(ch>=1 && ch<=9)
	    {
	       d1[j++]=s[i];
	    }
	    }
	}
	strcat(d1,d2);
	printf("%s",d1);
	return 0;
}