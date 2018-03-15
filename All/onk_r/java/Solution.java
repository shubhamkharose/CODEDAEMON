import java.util.*;
public class Solution
{
  static SortedSet<String> citiesSet;

  public static void main(String[] args) {
    String[] cities = { "Onk_r", "jagannath", "sathe", "2015", "BCS", "010" };

    citiesSet = new TreeSet<String>();
    for (String city : cities)
      citiesSet.add(city);


    for (String city : citiesSet)
      System.out.println("  " + city);
  }

}