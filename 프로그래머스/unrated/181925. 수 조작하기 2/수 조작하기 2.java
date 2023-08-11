import java.util.*;
class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        Map<Integer, String> dict = new HashMap<>(){{
            put(1,"w"); put(-1,"s"); put(10,"d"); put(-10,"a"); 
        }};
        for (int idx = 0; idx < numLog.length -1; idx++){
            int val = numLog[idx +1] - numLog[idx];
            answer += dict.get(val);
        }
        return answer;
    }
}