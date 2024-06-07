import java.util.*; //arraylist, set, HashSet을 사용하기 위해 util함수가 필요

class Solution {
    public int solution(int n) {
        ArrayList<Integer> l = new ArrayList<>();
        for(int i = 1; i<= (int) Math.sqrt(n); i++){
               if (n % i == 0){
                   l.add(i);
                   l.add(n/i);
               }
        }
        Set<Integer> set = new HashSet<>(l);
        int result= 0;
        for(int s : set){
            result += s;
        }
        return result;
    }
}