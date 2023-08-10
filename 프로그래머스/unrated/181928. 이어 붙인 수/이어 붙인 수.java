class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        String Odd = ""; String Even = "";
        for (int i = 0 ; i < num_list.length; i++){
            if (num_list[i] % 2 == 1){
                Odd += Integer.toString(num_list[i]);
            }
            else{
                Even += Integer.toString(num_list[i]);
            }
        }
        return (Integer.parseInt(Odd) + Integer.parseInt(Even));
    }
}