//1. pQ 사용 X 전체 정렬 안 해주기 때문 -> treeSet 사용으로 변경 
//2. bfs에서 TreeSet.get()에서 null처리 추가 

import java.util.*;

public class Main {
    private static Map<Integer, TreeSet<Integer>> road = new HashMap<>();
    private static int[] visited;
    private static int IDX = 1;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String[] input_ = sc.nextLine().split(" ");
        int N = Integer.parseInt(input_[0]);
        int M = Integer.parseInt(input_[1]);
        int R = Integer.parseInt(input_[2]);
        visited = new int[N+1];
        
        for(int i=0;i<M;i++){
            String[] inputM_ = sc.nextLine().split(" ");
            int start = Integer.parseInt(inputM_[0]);
            int end = Integer.parseInt(inputM_[1]);
            TreeSet<Integer> tempS = road.getOrDefault(start, new TreeSet<>());
            tempS.add(end);
            road.put(start, tempS);
            
            TreeSet<Integer> tempE = road.getOrDefault(end, new TreeSet<>());
            tempE.add(start);
            road.put(end, tempE);
            
        }
        
        dfs(R);
        
        for(int i=1; i<visited.length; i++){
            System.out.println(visited[i]);
        }
    }
    
    private static void dfs(int now){
        visited[now] = IDX++;
        for(int r:road.getOrDefault(now, new TreeSet<>())){ 
            if (visited[r] == 0) dfs(r);
        } 
    }
}
