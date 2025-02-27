// dp[i][j] = dp[i-1][j-1]+dp[i-1][j]

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] N_K = sc.nextLine().split(" ");
        int N = Integer.parseInt(N_K[0]);
        int K = Integer.parseInt(N_K[1]);
        int[][] dp = new int[N][N];
        dp[0][0] = 1;
        for(int i=1;i<N;i++){
            dp[i][0] = 1;
            dp[i][i] = 1;
        }
        for(int i=2;i<N;i++){
            for(int j=1;j<i;j++){
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j];
            }
        }
        System.out.println(dp[N-1][K-1]);
    }
}
