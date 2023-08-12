import java.util.*;

class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = new int[queries.length];
        for (int idx = 0; idx < queries.length; idx++){
            ArrayList<Integer> list = new ArrayList<>();
            int s = queries[idx][0];
            int e = queries[idx][1];
            int k = queries[idx][2];
            for (int j = s; j <= e; j++){
                if (arr[j] > k){
                    list.add(arr[j]);
                }
            }
            if (list.size() == 0){
                answer[idx] = -1;
            }
            else{
                int min_num = 100000000;
                for (int num : list){
                    min_num = Math.min(num,min_num);
                }
                answer[idx] = min_num;
            }
        }
        
        return answer;
    }
}