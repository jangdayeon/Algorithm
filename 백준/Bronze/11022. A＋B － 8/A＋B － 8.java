import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int cnt = sc.nextInt();
        
        for(int i=1;i<=cnt;i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            
            System.out.println("Case #"+i+": "+x+" + "+y+" = "+(x+y));
        }
    }
}