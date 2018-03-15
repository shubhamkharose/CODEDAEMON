#include <stdio.h>
#include <string.h>
#include<math.h>
int main()
{
    int long dec_no;
      
	int i=-1, temp=0, j=0;
	char hexadecimal[20];
	
	printf("Enter a decimal number :");
	scanf("%ld", &dec_no);
	
	quotient = dec_no;
	
	while(quotient != 0)
	{
		temp = quotient % 16;
		
		if(temp < 10)
			temp = temp + 48;
		
		else
			temp = temp + 55;
		i++;
		hexadecimal[i] = temp;
		quotient = quotient / 16;
	}
 
	printf("Hexadecimal value is\n");
	for(j = i; j>=0; j--)
          
      
      
}
