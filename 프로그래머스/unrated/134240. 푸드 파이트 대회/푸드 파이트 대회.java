class Solution {
    public String solution(int[] food) {
        String answer = "";
        for (int index = 1; index < food.length; index++){
            if (food[index] % 2 == 1){
                food[index] -= 1;
            }
            answer += String.valueOf(index).repeat(food[index] / 2);
        }
        answer += '0';
        for (int idx = answer.length() -2; idx >= 0 ; idx--){
            answer += answer.charAt(idx);
        }
        return answer;
    }
}