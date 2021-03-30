  import java.io.*;
  import java.util.*;
  import java.text.*;
  import java.math.*;
  import java.util.regex.*;

  public class Solution {

      public static void main(String[] args) {
          Scanner in = new Scanner(System.in);
          int t = in.nextInt();
          for(int a0 = 0; a0 < t; a0++){
              long n = in.nextLong();
              long num1 = 1;
              long num2 = 2;
              long num3 = 0;
              long result=2;
              for(long i=0; i<n; i+=num1){
                  num3 = num1+num2;

                  if(num3%2==0){
                      result+=num3;
                  }

                  num1=num2;
                  num2=num3;

              }
              System.out.println(result);
          }
      }
  }
