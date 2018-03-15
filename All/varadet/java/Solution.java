import java.util.*;
class Solution
{
    public static void main(String []args){
        int t=0;
        Scanner sc=new Scanner(System.in);
        t=sc.nextInt();
        while(t-->0)
        {
            String str="";
            str=sc.next();
            int l=str.length();
            int i=0,flg=0;
            int cnt1=0;
            char []arr=str.toCharArray();
            int cnt[]=new int[26];
            for(i=0;i<l;i++){
                cnt[arr[i]-97]++;
            }
            for(i=0;i<26;i++){
                if(cnt[i]==1)
                    cnt1++;
            }
            if(cnt1==1||cnt1==0)
                System.out.println("YES");
            else
                System.out.println("NO");
        }
    }

}