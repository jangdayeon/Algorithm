import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = Integer.parseInt(sc.nextLine());
        
        char[][] board = new char[3][3];
        for(int i=0; i<N; i++){
            char[] seed = sc.nextLine().toCharArray();
            for(int j=0; j<3; j++){
                board[j] = sc.nextLine().toCharArray();            
            }
            String score = getScore(seed, board, new int[3][3]);
            String rtnSeed = getFirstSeed(score, seed, board);
            System.out.println(score+" "+rtnSeed);
        }
    }
    public static String getFirstSeed(String score, char[] seed, char[][] board){
        //나머지 문자열 조합 만들기
        List<char[]> permutations = new ArrayList<>();
        char[] rst = new char[seed.length];
        Arrays.sort(seed);
        setPermutation(permutations, seed, new boolean[seed.length], 0, seed.length, rst);
        for(char[] pmt : permutations){
            String nowScore = getScore(pmt, board, new int[3][3]);
            if(score.equals(nowScore)) return String.valueOf(pmt);
        }
        return "";
    }
    
    private static void setPermutation(List<char[]> permutations, char[] seed, boolean[] visited, int r, int dept, char[] nowSeed){
        if(r==dept){
            permutations.add(nowSeed.clone());
            return;
        }
        for(int i=0; i<dept; i++){
            if(visited[i]) continue;
            nowSeed[r] = seed[i];
            visited[i] = true;
            setPermutation(permutations, seed, visited, r+1, dept, nowSeed);
            visited[i] = false;
        }
    }
    
    public static String getScore(char[] seed, char[][] board, int[][] visited){
        StringBuilder sb = new StringBuilder();
        int cntNowBingo = 0;
        int cntAllBingo = 0;
        for(int i=0; i<seed.length; i++){
            //현재 알파벳 위치 찾기
            int x=-1; int y=-1;
            for(int j=0; j<board.length; j++){
                for(int z=0; z<board[0].length; z++){
                    if(board[j][z] == seed[i]) {
                        x = j; y = z;
                        break;
                    }
                }
            }
            
            //색 칠하기(visited = 1)
            visited[x][y] = 1;
            // System.out.println(bingo);
            cntNowBingo = cntBingo(visited, cntAllBingo);
            cntAllBingo += cntNowBingo;
            sb.append(cntNowBingo);
        }
        return sb.toString();
    }
    public static int cntBingo(int[][] v, int before){
        int rtn = 0;
        //가로 빙고일 경우
        for(int i=0; i<3; i++){
            if((v[i][0] == 1)
            && (v[i][1] == 1)
            && (v[i][2] == 1)){
                    rtn++;
            }
        }
        //세로 빙고일 경우
        for(int i=0; i<3; i++){
            if((v[0][i] == 1)
            && (v[1][i] == 1)
            && (v[2][i] == 1)){
                    rtn++;
            }
        }
        //주-대각선일 경우
        if((v[0][0] == 1)
            && (v[1][1] == 1)
            && (v[2][2] == 1)){
                    rtn++;
        }
        //반-대각선일 경우
        if((v[0][2] == 1)
            && (v[1][1] == 1)
            && (v[2][0] == 1)){
                    rtn++;
        }
        return rtn-before;
    }
}
