//약간 효율적인 화폐 구성 문제랑 유사
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] NK = sc.nextLine().split(" ");
        int N = Integer.parseInt(NK[0]), K = Integer.parseInt(NK[1]);
        int[] nums = new int[N];
        int[] dp = new int[K+1];
        dp[0] = 1;
        
        for(int i=0; i<N; i++){
            nums[i] = Integer.parseInt(sc.nextLine());
        }
        
        for(int i=0; i<N; i++){
            for(int j=nums[i]; j<K+1; j++){
                dp[j] += dp[j-nums[i]];
            }
        }
        
        System.out.println(dp[K]);
        // System.out.println(Arrays.toString(dp));  
    }
}
