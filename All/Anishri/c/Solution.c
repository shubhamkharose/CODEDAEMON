#include <stdio.h>
#include<string.h>
int comparitor(const void *a,const void *b)
{
    return(*(char*)a-*(char*)b);
}
int main()
{
	//type here
	char s[10001];
	scanf("%s",s);
	int cnt=0;
    for(int i=0;s[i]!='\0';i++)
    {
        cnt++;
    }
	qsort(s,cnt,sizeof(char),comparitor);
	printf("%s",s);
	return 0;
}