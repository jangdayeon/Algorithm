//입력값
// 3
// 4
// 1 2 1 2

// 기댓값
// 1 2
//이것땜에 계속^^.. 0 1 2로 나왔어서,,ㅎ


//우선순위 큐 사용한 구현 문제

import java.util.Arrays;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;

class Student implements Comparable<Student> {
	String number;
	int recommend;
	int update;

	Student(String number, int recommend, int update) {
		this.number = number;
		this.recommend = recommend;
		this.update = update;
	}

	@Override
	public int compareTo(Student student) {
		return this.recommend != student.recommend ? this.recommend - student.recommend : this.update - student.update;
	}

	@Override
	public String toString() {
		return "Student{" +
			"number='" + number + '\'' +
			", recommend=" + recommend +
			", update=" + update +
			'}';
	}
}

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		int N = Integer.parseInt(scanner.nextLine());
		int len = Integer.parseInt(scanner.nextLine());
		String[] students = scanner.nextLine().split(" ");

		PriorityQueue<Student> board = new PriorityQueue<>();
		Set<String> isExist = new HashSet<>();
		int timer = 0;

		for (String num : students) {
			//틀에 넣을 수 없을 경우
			if (N == 0) {
                if(!isExist.contains(num)){
                    Student stu = board.poll();
                    isExist.remove(stu.number);
	                N += 1;	
                }		
			}
			//틀에 넣을 수 있을 경우
			if (isExist.contains(num)) {
				Student stu = board.stream().filter(student -> student.number.equals(num)).findFirst().get();
				board.remove(stu);
				stu.recommend += 1;
				board.add(stu);
			} else {
				board.add(new Student(num, 1, timer++));
				isExist.add(num);
                N -= 1;
			}
		}
        
        int[] answer = isExist.stream().mapToInt(Integer::parseInt).toArray();
        Arrays.sort(answer);
        
		for (int a : answer) {
			System.out.print(a + " ");
		}

	}
}