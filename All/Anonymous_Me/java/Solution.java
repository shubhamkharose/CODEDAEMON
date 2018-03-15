import java.util.*;
class PalindromeChecker {  
public static boolean isPalindrome(String str){  
    StringBuilder sb=new StringBuilder(str);  
    sb.reverse();  
    String rev=sb.toString();  
    if(str.equals(rev)){  
        return true;  
    }else{  
        return false;  
    }  
}  
}  

class Solution {  
public static void main(String[] args) {  
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    for(int i=0;i<n;i++)
    {
        String st=sc.next();
        if(PalindromeChecker.isPalindrome(st))
            System.out.println("YES");
        else
            System.out.println("NO");
    }
}  
}  