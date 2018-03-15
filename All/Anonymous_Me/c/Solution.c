#include <stdio.h>
#include<string.h>
int main() {
	char a[1001];
	int i,len,flag=0;
	int n;
	scanf("%d",&n);
	while(n>0)
    {
	    fgets(a,1001,stdin);
	    len=strlen(a);
	    for (i=0;i<len;i++) {
		    if(a[i]==a[len-i-1])
		        flag=flag+1;
	        }
	if(flag==len)
	             printf("YES\n"); else
	             printf("NO\n");
	       n--;
    }
	return 0;
}