import java.util.Scanner;
class Solution
{
        public static void main(String []args)
        {
                 Scanner sc = new Scanner(System.in);
                 //Enter your code here
                 int tc=sc.nextInt();
                 while(tc-- > 0){
                     String s=sc.next();
                     StringBuilder sb=new StringBuilder(s);
                     sb=sb.reverse();
                     if(s.equals(""+sb) == true)
                        System.out.println("YES");
                     else
                     System.out.println("NO");
                 }
        }
}