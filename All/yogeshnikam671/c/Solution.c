#include <stdio.h>

int main() {
	//code
	int n,h[10],d[10];int t;int i=0,j=0,l=0;int k;
	int num[20],denum=6,o;int denuma[20];
	int nump=1,denump=1;
	int p;int cnt=1;int x,y;
	int m=0,b=0;
	printf("\n Enter the number of test cases:");
	scanf("%d",&t);
	if(t>10)return 0;
	for(i=0;i<t;i++)
	{
	    printf("\n Enter no. of obstacles:");
	    scanf("%d",&n);n=(2*n)+1;
	    for(k=n;k<n;k++)
	    {
	        if(k%2==1||k==1)
	        {
	            scanf("%d",&h[j]);
	            j++;
	            
	        }
	        else
	        {
	            scanf("%d",&d[l]);
	            l++;
	            
	        }
	        
	    }
	    for(o=l;o>=0;o--)
	    {
	        while(d[o]>6)
	        {
	            d[o]=d[o]-6;
	            denum*=6;
	        }
	        num[m]=d[o];denuma[b]=denum;
	        m++;b++;
	    }
	    for(p=j;p>=0;p--)
	    {
	        cnt=1;
	        while(h[p]>6)
	        {
	            h[p]=h[p]-6;
	            denum*=6;
	        }
	        if(h[p]<6)
	        {
	            while(h[p]!=6)
	            {
	              cnt++;
	              h[p]++;
	            }
	        }
	        else
    	   {
    	       if(h[p]==6)
    	        cnt=1;
    	       
    	   }
    	    num[m]=cnt;
	        denuma[b]=denum;
	        m++;b++;
	        
	    }
	    x=m;y=b;
	    for(x=m;x>=0;x--)
	    {
	        nump*=num[x];
	        
	    }
	    for(y=b;y>=0;y--)
	    {
	        denump*=denuma[y];
	  
	    }
	    printf("%d/%d",num[1],denuma[1]);
	    
	    
	    
	    
	    
	    
	    
	    
	}
	
	return 0;
}