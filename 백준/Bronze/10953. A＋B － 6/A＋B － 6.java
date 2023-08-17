import java.util.Scanner;
import java.lang.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int cnt = sc.nextInt();
        for(int i=0;i<cnt;i++){
        String str = sc.next();
        String[] arr = str.split(",");
        int a = Integer.parseInt(arr[0]);
        int b = Integer.parseInt(arr[1]);
        System.out.println(a+b);
        }
    }
}