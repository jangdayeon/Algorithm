// e+(15*a) == s+(28*b) == m+(19*c) == year
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		int year = 1;
		while(true) {
			if(((year-Integer.parseInt(str[0])) % 15 == 0) && ((year-Integer.parseInt(str[1])) % 28 == 0) && ((year-Integer.parseInt(str[2])) % 19 == 0)){
				System.out.println(year);
				return;
			} else {
				year += 1;
			}
		}
	}
}
