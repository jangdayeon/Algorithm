class Solution {
    public int solution(String skill, String[] skill_trees) {
        String regex = "[^"+skill+"]";
        
        for(int i = 0;i<skill_trees.length;i++){
            skill_trees[i] = skill_trees[i].replaceAll(regex,"");
        }
        
        int rtn = 0 ;
        for(String s : skill_trees){
            if(s.equals("")) rtn += 1;
            for(int i = 0; i<s.length();i++){
                if(!(skill.charAt(i) == s.charAt(i))){
                    break;
                }
                if(i == s.length() - 1) rtn += 1;
            }
        }
        return rtn;   
    }
}