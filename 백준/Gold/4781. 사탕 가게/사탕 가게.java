import java.util.*;
class Candy{
    int calories;
    int price;
    
    public Candy(int calories, float price){
        this.calories = calories;
        this.price = (int)(price*100+ 0.5);//반올림을 통해 오차해결
    }
    
    @Override
    public String toString(){
        return calories+" "+price;
    }
}
public class Main {
    public static int[] dp;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(true){
            String[] NM = sc.nextLine().split(" ");
            if(NM[0].equals("0") && NM[1].equals("0.00")){
                break;
            }
            
            int N = Integer.parseInt(NM[0]);
            int M = (int)(Float.parseFloat(NM[1])*100+ 0.5);
            
            List<Candy> candys = new ArrayList<>();
            dp = new int[M+1];
            for(int i=0; i<N; i++){
                String[] CP = sc.nextLine().split(" ");
                int C = Integer.parseInt(CP[0]);
                float P = Float.parseFloat(CP[1]);
                
                candys.add(new Candy(C,P));
            }
            
            //dp의 index = 최대 가격, value = 칼로리
            for(int i=0; i<N; i++){
                Candy now = candys.get(i);
                for(int j=now.price; j<M+1; j++){
                    dp[j] = Math.max(dp[j], now.calories+dp[j-now.price]);
                }
            }
            System.out.println(dp[M]);
        }
    }
}    
