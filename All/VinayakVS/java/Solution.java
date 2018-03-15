import java.util.Scanner;
public class Solution
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    String operand=sc.next();
	    String s1=sc.next();
	    String s2=sc.next();
	    long a,b,c=0;
	    a=Long.parseLong(s1,16);
	    b=Long.parseLong(s2,16);
	    if(operand.equals("+"))
	    {
	       c=a+b;
	    }else if(operand.equals("-"))
	    {
	        c=a-b;
	    }
	    else if(operand.equals("*"))
	    {
	        c=a*b;
	    }
	    else if(operand.equals("/"))
	    {
	        c=a/b;
	    }
	    else if(operand.equals("%"))
	    {
	        c=a%b;
	    }
	    else
	    {
	        if(operand.equals("$") || operand.equals("^"))
	    {
	        c=(long)Math.pow(a,b);
	    }
	    }
	    System.out.println(Long.toHexString(c) );
	}
}