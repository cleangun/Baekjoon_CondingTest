import java.util.ArrayList;
class Solution {
    public int[] solution(int l, int r) {
        int[] answer = {};
        ArrayList<Integer> numlist = new ArrayList<Integer>();
        outerLoop:
        for (int i = l; i <= r; i ++){
            String num = String.valueOf(i);
            for (int idx = 0; idx < num.length(); idx++){
                if (num.charAt(idx) == '0' || num.charAt(idx) == '5'){
                    continue;
                }
                else{
                    continue outerLoop;
                }
            }
            numlist.add(Integer.valueOf(num));
        }
        System.out.println(numlist);
        return numlist.size() == 0 ? new int[]{-1} : numlist.stream().mapToInt(Integer::intValue).toArray();
    }
}