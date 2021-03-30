import java.io.*;
import java.util.*;
import java.math.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        scan.nextLine();
        BigInteger result = new BigInteger("0");
        for(int i=0; i<num; i++){
            String bigNum = scan.nextLine();
            BigInteger bigInteger = new BigInteger(bigNum);
            result = result.add(bigInteger);
                
        }
        
        String finalResult = result.toString();
        System.out.println(finalResult.substring(0,10));


        
    }
}
