//컨테이너 : 큐
//보조 : 스택

import java.util.*;
class Solution {
    public int solution(int[] order) {
        Queue<Integer> q = new LinkedList<>();
        for(int i=0;i<order.length;i++){
            q.add(i+1);
        }
        Stack<Integer> s = new Stack<>();
        
        int answer = 0;
        int need = 0;
        while(q.peek()!=null){
            if (order[need] == q.peek()){
                q.poll();
                need +=1;
                answer +=1;
            }
            else if(!s.empty()){
                if(order[need] == s.peek()){
                    s.pop();
                    need +=1;
                    answer +=1;
                }
                else{
                    s.push(q.poll());
                }
            }
            else{
                s.push(q.poll());
            }
        }
        
        
        while(!s.empty()){
            if(s.peek()==order[need]){
                s.pop();
                answer +=1;
                need +=1;
            }
            else{
                break;
            }
        }
        
        return answer;
    }
}