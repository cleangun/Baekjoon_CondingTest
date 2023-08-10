import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length + 1];
        for (int i = 0; i < num_list.length; i++){
            answer[i] = num_list[i];
        }
        int length = answer.length;
        answer[length - 1] = (num_list[length - 2] > num_list[length - 3]) ? 
            num_list[length - 2] - num_list[length - 3] : num_list[length - 2] * 2;
        return answer;
    }
}