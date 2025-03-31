//합의 성질 이용

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        String[] nums_ = sc.nextLine().split(" ");
        long[] nums = new long[N];
        for(int i=0;i<N;i++){
            nums[i] = Long.parseLong(nums_[i]);
        }
        long answer = 0;
        long now = 0;
        for(int i=0; i<N; i++){
            now += nums[i];
        }
        for(int i=0; i<N;i++){
            now -= nums[i];
            answer += nums[i] * now;
        }
        System.out.println(answer);
    }
}
