import java.util.*;
// Java program to print all possible strings of length k
class Solution {
    static long le=100000;
    static String sp;
    
    static int longestPalSubstr(String str) {
        int maxLength = 1; // The result (length of LPS)
 
        int start = 0;
        int len = str.length();
 
        int low, high;
 
        // One by one consider every character as center
        // point of even and length palindromes
        for (int i = 1; i < len; ++i) 
        {
            // Find the longest even length palindrome with 
            // center points as i-1 and i.
            low = i - 1;
            high = i;
            while (low >= 0 && high < len
                    && str.charAt(low) == str.charAt(high)) {
                if (high - low + 1 > maxLength) {
                    start = low;
                    maxLength = high - low + 1;
                }
                --low;
                ++high;
            }
 
            // Find the longest odd length palindrome with 
            // center point as i
            low = i - 1;
            high = i + 1;
            while (low >= 0 && high < len
                    && str.charAt(low) == str.charAt(high)) {
                if (high - low + 1 > maxLength) {
                    start = low;
                    maxLength = high - low + 1;
                }
                --low;
                ++high;
            }
        }
    
        return maxLength;
    }
 
    // Driver method to test below methods
    public static void main(String[] args) {             
        
        char set1[] = {'a', 'b'};
        int k = 8;
        printAllKLength(set1, k);
        
    }    
 
    // The method that prints all possible strings of length k.  It is
    //  mainly a wrapper over recursive function printAllKLengthRec()
    static void printAllKLength(char set[], int k) {
        int n = set.length;        
        printAllKLengthRec(set, "", n, k);
    }
    
    // The main recursive method to print all possible strings of length k
    static void printAllKLengthRec(char set[], String prefix, int n, int k) {
         
        // Base case: k is 0, print prefix
        if (k == 0) {
            long d=longestPalSubstr(prefix);
            if(d==3){
                System.out.println(prefix);
                //System.exit(0);
            }
            return ;
        }
 
        // One by one add all characters from set and recursively 
        // call for k equals to k-1
        for (int i = 0; i < n; ++i) {
             
            // Next character of input added
            String newPrefix = prefix + set[i]; 
             
            // k is decreased, because we have added a new character
            printAllKLengthRec(set, newPrefix, n, k - 1); 
        }
    }
}