class Solution {
    public String solution(String code) {
        int mode = 0;
        String answer = "";
        for (int idx = 0; idx < code.length(); idx++){
            char alphabet = code.charAt(idx);
            if (alphabet == '1'){
                mode = mode == 1 ? 0 : 1;
                continue;
            }
            if (idx % 2 == mode){
                answer += alphabet;
            }
        }
        return answer.length() == 0? "EMPTY" : answer;
    }
}