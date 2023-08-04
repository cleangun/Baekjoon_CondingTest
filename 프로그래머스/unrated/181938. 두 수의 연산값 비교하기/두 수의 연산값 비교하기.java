class Solution {
    public int solution(int a, int b) {
        int along = Integer.parseInt(""+a+b);
        int blong = 2 * a * b;
        return along > blong ? along : blong;
    }
}