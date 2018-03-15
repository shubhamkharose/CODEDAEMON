#include <stdio.h>
#include <string.h>
int main()
{
     
     int a,b,c;
     int t;
     scanf("%d",&t);
     int i;
     for(i=0;i<t;i++)
     {
         int max=0,x=0;
        scanf("%d %d %d",&a,&b,&c);
        if(a>b)
	{
		if(a>c)
		    max=a;
		else
			max=c;
	}
	else
	{
		if(b>c)
			max=b;
		else
			max=c;
	}
	if(max==a)
	    x=1;
	else if(max==b)
	    x=2;
	else
	    x=3;
        switch(x)
        {
            case 1:
                if(b*b+c*c==a*a)
                    printf("right\n");
                else if(b*b+c*c>a*a)
                    printf("acute\n");
                else
                    printf("obtuse\n");
                break;
            case 2:
                if(b*b==c*c+a*a)
                    printf("right\n");
                else if(b*b<c*c+a*a)
                    printf("acute\n");
                else
                    printf("obtuse\n");
                break;
            case 3:
                if(b*b+a*a==c*c)
                    printf("right\n");
                else if(b*b+a*a>c*c)
                    printf("acute\n");
                else
                    printf("obtuse\n");
                break;
        }
        
     }
     return 0;//type your code here
}
