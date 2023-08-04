class Solution {
    public int solution(int a, int b) {
        int 후보1 = Integer.valueOf(String.valueOf(a) + String.valueOf(b));
        int 후보2 = Integer.valueOf(String.valueOf(b) + String.valueOf(a));
        return Math.max(후보1,후보2);
    }
}