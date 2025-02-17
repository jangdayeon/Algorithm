import java.util.*;
class Main {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int len = scanner.nextInt();
		Deque<Integer> list = new LinkedList<>();
		StringBuilder sb = new StringBuilder();
		for (int i = 1; i <= len; i++) {
			list.add(i);
		}

		while(list.size()>1){
			int first = list.pollFirst();
			sb.append(first);
			sb.append(" ");
			int second = list.pollFirst();
			list.addLast(second);
		}
		sb.append(list.getFirst());
		System.out.println(sb.toString());
	}
}
