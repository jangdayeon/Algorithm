import java.util.*;

public class Main {
    static int R;
    static int C;
    static int[][] pixels;
    static int[] J;
    static int T;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String[] RC = sc.nextLine().split(" ");
        R = Integer.parseInt(RC[0]);
        C = Integer.parseInt(RC[1]);
        pixels = new int[R][];
        J = new int[(R-2)*(C-2)];
        int JIdx = 0;
        
        for(int i=0; i<R; i++){
            String[] pixels_ = sc.nextLine().split(" ");
            pixels[i] = Arrays.stream(pixels_)
                            .mapToInt(Integer::parseInt)
                            .toArray();
        }
        
        T = Integer.parseInt(sc.nextLine());
        
        for(int i=0; i<R-2; i++){
            for(int j=0; j<C-2; j++){
                int[] temp = new int[9];
                int idx = 0;
                for(int a=i; a<i+3; a++){
                    for(int b=j; b<j+3; b++){
                        temp[idx++] = pixels[a][b];
                    }
                }
                Arrays.sort(temp);
                J[JIdx++] = temp[4];
            }
        }
        
        int answer = 0;
        for(int jj : J){
            if(jj >= T) answer++;
        }
        System.out.println(answer);
    }
}
