import java.util.Scanner;

class Main {
	static String[][] board;

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		String[] nAndMAndR = scanner.nextLine().split(" ");
		board = new String[Integer.parseInt(nAndMAndR[0])][Integer.parseInt(nAndMAndR[1])];
		for (int i = 0; i < Integer.parseInt(nAndMAndR[0]); i++) {
			board[i] = scanner.nextLine().split(" ");
		}
		for (int i = 0; i < Integer.parseInt(nAndMAndR[2]); i++) {
			for (int j = 0; j < Math.min(Integer.parseInt(nAndMAndR[0]),Integer.parseInt(nAndMAndR[1])) / 2; j++) {
				rotate(j);
			}
		}
		print();
	}

	public static void rotate(int s) {
		String temp;
		//상
		temp = board[s][s];
		for (int i = s + 1; i < board[0].length - s; i++) {
			board[s][i - 1] = board[s][i];
		}
		//우
		for (int i = s + 1; i < board.length - s; i++) {
			board[i - 1][board[0].length - s - 1] = board[i][board[0].length - s - 1];
		}
		//하
		for (int i = board[0].length - s - 1; i > s; i--) {
			board[board.length - s - 1][i] = board[board.length - s - 1][i - 1];
		}
		//좌
		for (int i = board.length - s - 1; i > s; i--) {
			board[i][s] = board[i - 1][s];
		}
		board[s + 1][s] = temp;
	}

	public static void print() {
		for (int i = 0; i < board.length; i++) {
			System.out.println(String.join(" ", board[i]));
		}
	}
}
