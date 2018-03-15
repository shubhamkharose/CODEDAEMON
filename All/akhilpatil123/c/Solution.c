#include <stdio.h>
int rr=-1,fr=0;
long int arr[50];
int main() {
	//code
	long int d[50]={0};
	int n,i=1;
	static int j=1;
	long int sum=0,sump;
	do 
	{
	    scanf("%ld",&d[i]);
	    i++;
	}while(d[i]!=EOF);
	scanf("%d",&n);
	while(1)
	{
	    for(;j<=j+3;j++)
	    {
	    sum+=d[j];
	    }
	    if(sum==0)
	        break;
        if(sump>10)
        {
            sum+=sump;
        }
	    arr[++rr]=sum;
	    sump=sum;
	} 
	while(fr<=rr)
	printf("%ld",arr[fr++]);
	return 0;
}