//전체 탐색 및 투 포인터 이용 -> 재귀 함수로 전체 탐색 구현
import java.util.*;

public class Main {
    private static int[] fruits; 
    private static Map<String, Integer> memo = new HashMap<>();
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        fruits = new int[N];
        String[] getFruits =sc.nextLine().split(" ");
        Map<Integer,Integer> totalCnt = new HashMap<>();
        for(int i=0; i<N; i++){
            fruits[i] = Integer.parseInt(getFruits[i]);
            totalCnt.put(fruits[i], totalCnt.getOrDefault(fruits[i], 0)+1);
        }
        System.out.println(maxLengthWithTwoTypes());
    }
    
    private static int maxLengthWithTwoTypes(){
        int left = 0;
        int maxLength = 0;
        Map<Integer, Integer> fruitCount = new HashMap<>();
        
        //right 포인터를 이용해 구간을 확장
        for(int right = 0; right < fruits.length; right++){
            fruitCount.put(fruits[right], fruitCount.getOrDefault(fruits[right],0)+1);
            
            //고유한 과일 종류가 3개 이상일 경우, left 포인터를 이동시켜 과일 종류를 2개 이하로 만들기
            while(fruitCount.size() > 2){
                fruitCount.put(fruits[left], fruitCount.get(fruits[left])-1);
                if(fruitCount.get(fruits[left]) == 0){
                    fruitCount.remove(fruits[left]);
                }
            left++; 
            }
        maxLength = Math.max(maxLength, right - left + 1); 
        }
        return maxLength;
    }
}
