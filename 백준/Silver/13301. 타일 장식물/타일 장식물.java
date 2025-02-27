import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        
        long even = 1L;
        long odd = 1L;
        for(int i=2; i<N+1; i++){
            if(i%2==0){
                even +=odd;
            } else{
                odd += even;
            }
        }
        
        System.out.println(even*2+odd*2);    
        
    }
}
