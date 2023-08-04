class Solution {
    public int solution(int a, int b) {
        int along = Integer.parseInt(""+a+b);
        int blong = Integer.parseInt(""+b+a);
        return along > blong? along : blong;
    }
}