import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		//1000개까지 메모이제이션 이용해서 1 ~ 1000개의 팰린드롬 개수 저장
		int[] memo = new int[1001];
		memo[1] = 1;
		memo[2] = 2;
		for (int i = 3; i < memo.length; i++) {
			int middle = i;
			int side = 0;
			int cnt = 0;
			while( middle - 2 > 0 ) {
				side += 1;
				middle -= 2;
				cnt += memo[side];
			}
			if(i % 2 == 0){ // 짝수이면,
				cnt += memo[i/2];
			}
			memo[i] = cnt + 1; //자기 자신 포함
		}


		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i < T; i++) {
			int N = Integer.parseInt(br.readLine());
			System.out.println(memo[N]);
		}
	}
}
