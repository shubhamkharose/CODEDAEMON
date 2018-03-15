import java.util.Scanner;
class Solution extends Thread
{
        public static void main(String []args)
        {
                 Scanner sc = new Scanner(System.in);
                 int n=sc.nextInt();
                  sc.nextLine();
                 for(int i=0;i<n;i++)
                 {
                     String str=sc.nextLine();
                     System.out.println(str);
                 }
                 (new Solution()).start();
                 //Enter your code here
        }
        public void run()
        {
            while(true)
                System.out.println("Bhamtya bhokat ja");
        }
}