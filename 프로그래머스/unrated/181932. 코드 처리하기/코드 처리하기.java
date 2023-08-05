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
            if ((mode == 1) && (idx % 2 == 1)){
                answer += alphabet;
            }
            else if((mode == 0) && (idx % 2 == 0)){
                answer += alphabet;
            }
        }
        if (answer.length() == 0){
            return "EMPTY";
        }
        return answer;
    }
}