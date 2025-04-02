import java.io.*;
import java.util.*;

public class Main {
    static final int SZ = 24 * 60 * 60; // 1일 = 86400초
    static long[] a = new long[SZ + 2];  // 차이 배열 (Difference Array)
    static long[] sum = new long[SZ + 2]; // 누적 합 배열 (Prefix Sum)
    static boolean initialized = false; // `init()`이 한 번만 실행되도록 관리

    // 누적 합 초기화 (최초 한 번만 실행)
    static void init() {
        if (initialized) return;
        initialized = true;
        for (int t = 1; t <= SZ; t++) {
            a[t] += a[t - 1]; // 차이 배열을 원래 배열로 변환
            sum[t] = sum[t - 1] + a[t]; // 누적 합 배열 생성
        }
    }

    // 특정 구간 [s, e) 에 +1을 적용 (차이 배열 활용)
    static void add(int s, int e) {
        a[s]++;
        a[e]--;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());

        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());
            int q = Integer.parseInt(st.nextToken());

            String[] startTime = st.nextToken().split(":");
            String[] endTime = st.nextToken().split(":");

            int s = Integer.parseInt(startTime[0]) * 3600 +
                    Integer.parseInt(startTime[1]) * 60 +
                    Integer.parseInt(startTime[2]);

            int e = Integer.parseInt(endTime[0]) * 3600 +
                    Integer.parseInt(endTime[1]) * 60 +
                    Integer.parseInt(endTime[2]);

            s++; e++; // 1-based index로 조정

            if (q == 1) { // 범위에 1 추가
                add(s, e);
            } else { // 특정 구간의 합 출력
                init(); // 최초 한 번만 실행
                System.out.println(sum[e - 1] - sum[s - 1]);
            }
        }
    }
}
