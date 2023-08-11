import java.util.*;

class Solution {
    public int solution(int n, String control) {
        Map<Character,Integer> dict = new HashMap<>(){{
            put('w',1);
            put('s',-1);
            put('d',10);
            put('a',-10);
        }};
        for (int idx = 0; idx < control.length(); idx++){
            n += dict.get(control.charAt(idx));
        }
        return n;
    }
}