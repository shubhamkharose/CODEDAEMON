import java.io.*;
import java.util.*;
import java.math.*;
class Solution
{
	public static void main(String []args)
	{
		int t=0,i=0,j=0,k=0,l=0,n=0;
        
		Scanner sc=new Scanner(System.in);
		t=sc.nextInt();
		for(i=0;i<t;i++){
		    String s=sc.next();
		    int[]a=new int[26];
		    Arrays.fill(a,0);
		    int flg=0;
		    for(j=0;j<s.length();j++)
		    {
		        a[s.charAt(j)-97]++;
		        
		    }
		    for(j=0;j<s.length();j++)
		    {
		        if(flg==0&&a[s.charAt(j)-97]==1)
		            flg=1;
		        else if(flg==1&&a[s.charAt(j)-97]==1)
		        {
		            break;
		        }
		    }
		    if(j>=s.length())
		        System.out.println("YES");
	        else
	            System.out.println("NO");
		}
		//BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	}
}