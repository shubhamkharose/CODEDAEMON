import java.io.*;
import java.util.*;
public class Solution 
{
    
    static String printValid(String s)
    {
        
        int []arr;
        int n=s.length();
        arr=new int[n];
        int i=0;
        
        while(i<n)
        {
            arr[i]=s.charAt(i);
            i++;
        }
        i=n-1;
        int l=0;
        while(i>=1)
        {
            l=2*arr[i];
            if(l<=9)
            
                arr[i-1]=l;
            else
            
            {
                int p=(l/10)+(l%10);
                
                arr[i-1]=arr[i-1]+p;
                
            }
            i--;
            
        }
        int j=0,sum=0;
        while(j<n)
        {
            sum+=arr[i];
            j++;
            
        }
        
        if((sum%10)==0)
            return "Valid";
        else
            return "Invalid";
        // System.out.println(sum);
        
        
        
    }

     public static void main(String []args) 
     {
         Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
       
        int i=0;
        String s="";
        try{
        while(i<t)
        {
           //  Number n=0;
           
           
            // n=(Integer.parseInt)(sc.next());
             s=sc.next();
             System.out.println(printValid(s));
        }
        }
        catch(Exception e){}
         
         //add your code here
        //  System.out.println("Techumen is on");
}
}