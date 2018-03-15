#include <stdio.h>
#include <string.h>
int main()
{
    char str1[1000],strnum[1000]={'\0'},strchar[1000]={'\0'};
	int i=0,j=0,k=0,chk;
    scanf("%s",str1);
    for(j=0;j<1000;j++)
    {
        if(str1[j]=='\0')
            break;
        chk=str1[j];
        if(chk>=48&&chk<=57)
        {strnum[i]=str1[j];
            i++;}
        
        
        else
        {
        strchar[k]=str1[j];
        k++;}
    }
    strcat(strnum,strchar);
    printf("%s",strnum);
    return 0;
    
}