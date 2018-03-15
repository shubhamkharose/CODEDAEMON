import java.util.*;
class Solution
{
        public static void main(String []args)
        {
            int t;
            Scanner sc = new Scanner(System.in);
            t = sc.nextInt();
            while(t-->0){
                String s = sc.next();
                if(s.equals(new StringBuilder(s).reverse().toString())){
                    System.out.println("YES");
                }
                else
                    System.out.println("NO");
            }
        }
}