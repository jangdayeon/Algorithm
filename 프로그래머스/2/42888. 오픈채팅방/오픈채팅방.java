import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        Map<String,String> m = new HashMap<>();
        for(int i=0;i<record.length;i++){
            String[] tmp = record[i].split(" ");
            if(!tmp[0].equals("Leave")) {
                m.put(tmp[1],tmp[2]);
            }
        }
        List<String> rtn = new ArrayList<>();
        for(int i=0;i<record.length;i++){
            String[] tmp = record[i].split(" ");
            switch(tmp[0]){
                    case "Enter"->rtn.add(m.get(tmp[1])+"님이 들어왔습니다.");
                    case "Leave"->rtn.add(m.get(tmp[1])+"님이 나갔습니다.");
            }
        }
        
        return rtn.toArray(new String[0]);
    }
}