// 전체 탐색으로 문제 해결
// 일단 행 열 다 탐색 -> 가장 많이 같은 색인 곳 확인
// 색이 다른 곳을 하나씩 넣어보면서 max값 구하기(전체 탐색)
// max 리턴

//문제 틀림 해결 1
//현재 방식은 "가장 많이 나온 색" 이 있는 행과 열을 저장하는데, 가장 긴 연속된 색이 반드시 그 행/열에 있는 것은 아님.

//문제 틀림 이유 2
//하나를 바꿨을 때 이전에 안됐던 것이 다음거에 맞게 연결하면 하나로 연결될 수도 있기 때문에, 하나 탐색할 때마다
//가장 긴 길이를 구해야 함. 그러지 못해 틀림. 아예 다른 방식으로 접근해야 함

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
	static int N;
	static char[][] board;
	static int maxLength = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		board = new char[N][N];

		for (int i = 0; i < N; i++) {
			board[i] = br.readLine().toCharArray();
		}

		// 보드에서 모든 위치에 대해 인접한 색을 교환하고 최대 길이 찾기
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				// 오른쪽과 교환
				if (j + 1 < N) {
					swap(i, j, i, j + 1);
					checkMaxCandy();
					swap(i, j, i, j + 1); // 원래대로 되돌리기
				}
				// 아래쪽과 교환
				if (i + 1 < N) {
					swap(i, j, i + 1, j);
					checkMaxCandy();
					swap(i, j, i + 1, j); // 원래대로 되돌리기
				}
			}
		}

		System.out.println(maxLength);
	}

	// 두 위치의 사탕을 교환하는 함수
	static void swap(int x1, int y1, int x2, int y2) {
		char temp = board[x1][y1];
		board[x1][y1] = board[x2][y2];
		board[x2][y2] = temp;
	}

	// 보드에서 가장 긴 연속된 색상 찾기
	static void checkMaxCandy() {
		// 행 체크
		for (int i = 0; i < N; i++) {
			int count = 1;
			for (int j = 1; j < N; j++) {
				if (board[i][j] == board[i][j - 1]) {
					count++;
				} else {
					maxLength = Math.max(maxLength, count);
					count = 1;
				}
			}
			maxLength = Math.max(maxLength, count);
		}

		// 열 체크
		for (int j = 0; j < N; j++) {
			int count = 1;
			for (int i = 1; i < N; i++) {
				if (board[i][j] == board[i - 1][j]) {
					count++;
				} else {
					maxLength = Math.max(maxLength, count);
					count = 1;
				}
			}
			maxLength = Math.max(maxLength, count);
		}
	}
}
