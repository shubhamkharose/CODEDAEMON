import java.util.Scanner;
class Solution
{
        public static void main(String []args)
        {
                 Scanner sc = new Scanner(System.in);
                 //Enter your code here
                 int cnt=1;
            int val=-1;
            while(sc.hasNext()){
                if(val == 0)
                break;
            String s=sc.nextLine();
            if(cnt !=0 )
            {
                val=Integer.parseInt(s);
                cnt=0;
            }
            else{
                System.out.println(s);
                val--;
            }

        }
    }
}