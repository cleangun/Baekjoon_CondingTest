class Solution {
    public String solution(String str1, String str2) {
        String answer = "";
        for (int index = 0; index < str1.length(); index++){
            answer += str1.charAt(index); answer += str2.charAt(index);
        }
        
        return answer;
    }
}