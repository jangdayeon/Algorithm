import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        String[] A_ = sc.nextLine().split(" ");
        int[] A = new int[N];
        for(int i=0; i<N; i++){
            A[i] = Integer.parseInt(A_[i]);
        }
        int[] dp = new int[N];
        for (int i = 0; i < N; i++) {
            dp[i] = A[i];  
        }
        for(int i=0; i<N; i++){
                for(int j=i;j>=0;j--){
                    if(A[j]<A[i]){
                        dp[i] = Math.max(dp[i], dp[j]+A[i]);
                    }
                }
            }
              
        int answer = 0;
        for(int d:dp){
            answer = Math.max(answer,d);
        }
        
        System.out.println(answer);
        // System.out.println(Arrays.toString(dp));
        }
}
