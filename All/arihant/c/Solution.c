#include <stdio.h>

int main() {
	int num, parts, i, j, n, sum=0, carry=0, s[100], cnt=0;
	scanf("%d", &num);
	scanf("%d", &parts);
	n=num;
	for(i=0; n!='\0'; i++, n/=10)
	{
	    sum=carry;
	    carry=0;
	    for(j=0; j<parts; j++, num/10)
	    {
	        sum+=num%10;
	    }
	    if(sum>=10)
	    {
	        sum=sum%10;
	        carry=sum/10;
	    }
	    s[i]=sum;
	    cnt++;
	}
	for(i=(cnt/parts); i>0; i--)
	{
	    printf("%d", s[i]);
	}
	return 0;
}