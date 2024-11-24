class Solution {
    public int solution(int m, int n, String[] board) {
        char[][] nb = new char[m][n];
        for(int i=0;i<m;i++){
            nb[i] = board[i].toCharArray();
        }
        
        int answer = 0;
        while(true){
            
            boolean[][] bb =new boolean[m][n];
            boolean flag = false;
            
            //제거해야하는 곳 찾기
            for(int i=1;i<m;i++){
                for(int j=1;j<n;j++){
                    if(nb[i][j]!= '-'
                        && nb[i][j]==nb[i-1][j-1]
                        && nb[i-1][j-1]==nb[i-1][j]
                        && nb[i-1][j]==nb[i][j-1]){
                        bb[i][j] = true;
                        bb[i-1][j-1] = true;
                        bb[i][j-1] = true;
                        bb[i-1][j] = true;
                        flag = true;
                    }
                }
            }
            
            if(!flag) return answer;
            
            //삭제된 곳 계산하기
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(bb[i][j]) answer +=1;
                }
            }
            
            //블록 제거하기
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    if(bb[i][j]) {
                        for(int k=i;k>0;k--){
                            //나를 기준으로 내 위에 있던 값을 하나씩 아래로 보내기
                            nb[k][j] = nb[k-1][j];
                        }
                        nb[0][j] = '-';
                    }
                }
            }
            
        }
    }
}