import java.util.*;
class Solution
{
	public static void main(String []ar){
		Scanner sc= new Scanner(System.in);
		String s= sc.nextLine();
		char tempArray[] = s.toCharArray();
        Arrays.sort(tempArray);
		System.out.println(tempArray);
	}
}