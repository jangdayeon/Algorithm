import java.util.*;
import java.util.regex.*;

class Solution {
    public String[] solution(String[] files) {
        List<String[]> divi = new ArrayList<>();
        
        String regex = "([A-z .-]+)([0-9]+)(.*)";
        Pattern p = Pattern.compile(regex);
        for(int i=0;i<files.length;i++){
            Matcher m = p.matcher(files[i]);
            if(m.find()){
                divi.add(new String[]{m.group(1),m.group(2),m.group(3)});
            }
        }
        
        divi.sort(Comparator.comparing((String[] o)->o[0],String::compareToIgnoreCase).thenComparingInt(o->Integer.parseInt(o[1])));
        
        String[] rtn = new String[files.length];
        for(int i=0;i<files.length;i++){
            rtn[i] = divi.get(i)[0] + divi.get(i)[1] + divi.get(i)[2];
        }
        
        return rtn;
    }
}