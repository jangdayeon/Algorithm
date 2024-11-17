class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        int vlI = Integer.parseInt(video_len.substring(0,2))*60+Integer.parseInt(video_len.substring(3));
        int posI = Integer.parseInt(pos.substring(0,2))*60+Integer.parseInt(pos.substring(3));
        int opsI = Integer.parseInt(op_start.substring(0,2))*60+Integer.parseInt(op_start.substring(3));
        int opeI = Integer.parseInt(op_end.substring(0,2))*60+Integer.parseInt(op_end.substring(3));
        
        
        for (String c : commands){
            
            if ( posI >= opsI && posI <= opeI ){
                posI = opeI;
            }
            
            if(c.equals("next")) {
                posI = posI + 10 > vlI ? vlI : posI + 10 ;
            }
            else {
                posI = posI - 10 < 0 ? 0 : posI - 10 ;
            }
        }
        
        if ( posI >= opsI && posI <= opeI ){
                posI = opeI;
            }
        
        String rtn = "";
        rtn += posI/60 < 10? "0"+posI/60 : posI/60;
        rtn += ":";
        rtn += posI%60 < 10? "0"+ (posI%60) : (posI%60);
        return rtn;
    }
}