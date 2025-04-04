import java.util.*;
public class Main {
    static int[] arr;
    static int[] output;
    static boolean[] visited;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        arr = new int[n];
        output = new int[n];
        visited = new boolean[n];
        for(int i=1; i<=n; i++){
            arr[i-1] = i;
        }
        permutation(arr.length,0);
    }
    public static void permutation(int r, int dept){
        if(dept == r) {
            for(int o : output){
                System.out.print(o+" ");
            }
            System.out.println();
            return;
        }
        for(int i=0;i<arr.length;i++){
            if(!visited[i]){
                visited[i] = true;
                output[dept] = arr[i];
                permutation(r, dept+1);
                visited[i] = false;
            }
        }
    }
}
