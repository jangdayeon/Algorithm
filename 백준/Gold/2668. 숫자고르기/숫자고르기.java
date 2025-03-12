//dfs로 문제 풀이

//인덱스 처음부터 접근하는데, 이어진 숫자를 줄줄히 꺼내어 끝이 날 때 까지
// 끝이 난다 = 전체 탐색 or 이미 방문한 값
//돌아 짝이 맞는 것은 answer 리스트에 추가한다.
//리스트 사이즈 + 리스트를 오름차순으로 정렬하여 리턴한다.
//효율을 위해 visited list도 하나 만들자
import java.util.*;

public class Main {
    private static int N;
    private static int[] nums;
    private static Set<Integer> answer = new TreeSet<>();
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = Integer.parseInt(sc.nextLine());
        nums = new int[N];
        for(int i=0;i<N;i++){
            nums[i] = Integer.parseInt(sc.nextLine());
        }
        
        for(int i=0; i< N; i++){
            Set<Integer> firstLineSet = dfs(i, new HashSet<>());
            Set<Integer> secondLineSet = new HashSet<>();
            for(int s : firstLineSet){
                secondLineSet.add(nums[s-1]);
            }
            if(secondLineSet.equals(firstLineSet)){
                answer.addAll(firstLineSet);
            }
        }
        
        System.out.println(answer.size());
        for(int a : answer){
            System.out.println(a);
        }
        
    }
    
    private static Set<Integer> dfs(int i, Set<Integer> nowVisited){
        if(nowVisited.size() == N || nowVisited.contains(i+1)){
            return nowVisited;
        }
        nowVisited.add(i+1);
        return dfs(nums[i]-1, nowVisited);
    }
}
