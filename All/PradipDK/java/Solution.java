import java.util.*;
import java.io.*;
class Solution
{
    public static void main(String []args){
        Scanner sc=new Scanner(System.in);
        int t=0;
        t=sc.nextInt();
        
        while(t!=0)
        {
            t--;
            int cnt=0;
            int ch[]=new int[26];
            String s="";
            s=sc.next();
           // System.out.println(""+s);
            if(s.length()==1)
                System.out.println("YES");
                else
                {
            for(int i=0;i<s.length();i++)
            {
                
                ch[s.charAt(i)-97]++;
               // System.out.println(" "+s.charAt(i));
                
            }
            for(int i=0;i<ch.length;i++)
            {
                if(ch[i]%2==1)
                    cnt++;
                
            }
            if(cnt==1||cnt==0)
            {
                System.out.println("YES");
            }
            else
                System.out.println("NO");
                }
        }
        
    }

}