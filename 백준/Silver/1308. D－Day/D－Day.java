import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] YMD1 = sc.nextLine().split(" ");
        int Y1 = Integer.parseInt(YMD1[0]);
        int M1 = Integer.parseInt(YMD1[1]);
        int D1 = Integer.parseInt(YMD1[2]);

        String[] YMD2 = sc.nextLine().split(" ");
        int Y2 = Integer.parseInt(YMD2[0]);
        int M2 = Integer.parseInt(YMD2[1]);
        int D2 = Integer.parseInt(YMD2[2]);

        if (Y2 - Y1 > 1000 || (Y2 - Y1 == 1000 && (M2 > M1 || (M2 == M1 && D2 >= D1)))) {
            System.out.println("gg");
            return;
        }

        int days = 0;

        if(Y1 != Y2){
            //시작 해 날짜 더하기
            for(int i=12; i>M1; i--){
                days += restOfTheMonth(Y1, i, 0);
            }
            days += restOfTheMonth(Y1, M1, D1-1);

            //중간 해 날짜 더하기
            for(int i=Y1+1; i<Y2; i++){
                for(int j=1; j<=12; j++){
                    days += restOfTheMonth(i, j, 0);
                }
            }

            //마지막 해 날짜 더하기
            for(int i=1; i<M2; i++){
                days += restOfTheMonth(Y2, i, 0);
            }
            days += D2-1;
        } else {
            if(M1 == M2) days += D2 - D1;
            else {
                days += restOfTheMonth(Y1, M1, D1-1);
                for(int i=M1+1; i<M2; i++){
                    days += restOfTheMonth(Y2, i, 0);
                }
                days += D2-1;
            }
        }

        System.out.println("D-"+days);

    }
    public static boolean isYoon(int y){
        if(y % 400 == 0 || (y % 4 == 0 && y % 100 != 0)) return true;
        else return false;
    }

    public static int restOfTheMonth(int y, int m, int d){
        switch(m){
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                return 31-d;
            case 2:
                if (isYoon(y)) return 29-d;
                else return 28-d;
            default :
                return 30-d;
        }
    }
}
