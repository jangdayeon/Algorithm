//점화식 dp[i] = dp[i-1] + 1 or 1
//몰라서 힌트를 얻었더니, 오름차순일 경우랑 내림차순일 경우를 나눠서 dp check를 해야한다는 것을 알게 됨
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());
        if(n==1 || n==2) {
            System.out.println(n);
            return;
        }
        
        String[] nums_ = sc.nextLine().split(" ");
        int[] nums = new int[n];
        for(int i=0; i<nums.length; i++){
            nums[i] = Integer.parseInt(nums_[i]);
        }
        
        int[] dp_asc = new int[n];
        int[] dp_desc = new int[n];
        dp_asc[0] = 1;
        dp_desc[0] = 1;
        //dp시작
        for(int i=1; i<n;i++){
            if(nums[i] > nums[i-1]){
                dp_asc[i] = dp_asc[i-1]+1;
                dp_desc[i] = 1;
            } else if(nums[i] < nums[i-1]){
                dp_desc[i] = dp_desc[i-1]+1;
                dp_asc[i] = 1;
            } else{
                dp_asc[i] = dp_asc[i-1]+1;
                dp_desc[i] = dp_desc[i-1]+1;
            }
        }
        
        int answer = 0;
        for(int i=0;i<n;i++){
            int max = Math.max(dp_asc[i], dp_desc[i]);
            answer = Math.max(answer, max);
        }
        
        System.out.println(answer);
    }
}
