import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		Queue<Integer> queue = new PriorityQueue<>();
		for (int i = 0; i < N; i++) {
			int[] num = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
			for(int n : num){
				queue.add(-n);
			}
		}
		for (int i = 0; i < N - 1; i++) {
			queue.poll();
		}
		System.out.println(-queue.peek());
	}
}
