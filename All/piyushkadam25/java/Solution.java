import java.util.*;
import java.lang.*;
import java.io.*;
import java.math.*;

/* Name of the class has to be "Main" only if the class is public. */
class Solution
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		for(int p=0;p<t;p++)
		{
		    int r=sc.nextInt();
		    int c=sc.nextInt();
		    int j=(r*c)+2;
		    int k=Integer.parseInt(""+Math.pow(2,j));
		    System.out.println(""+k);
		}
	}
}
