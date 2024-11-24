class Solution {
    public int solution(int[] mats, String[][] park) {
        int[][] n_park = new int[park.length][park[0].length];
        for(int i=0;i<park.length;i++){
            for(int j=0;j<park[0].length;j++){
                if(park[i][j].equals("-1")){
                    n_park[i][j] = 1;
                }
            }
        }

        int answer = -1;
        for(int i=1;i<park.length;i++){
            for(int j=1;j<park[0].length;j++){
                if(n_park[i][j]==1 && (n_park[i-1][j-1]!=0 && n_park[i-1][j]!=0&&n_park[i][j-1]!=0)){
                    n_park[i][j] += Math.min(n_park[i-1][j-1],Math.min(n_park[i-1][j],n_park[i][j-1]));
                }
                
                for(int m : mats){
                    if(m == n_park[i][j]) answer = Math.max(m,answer);
                }
            }
        }
        
        return answer;
    }
}