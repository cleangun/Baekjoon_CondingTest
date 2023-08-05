class Solution {
    public int solution(int a, int b, int c) {
        int count = 0; int answer = 1;
        if (a == b && a == c){
            count = 2;
        }
        else if (a == b || a == c){
            count = 1;
        }
        else if (b == c){
            count = 1;
        }
        for (int i = 0; i < count+1; i++){
            answer *= Math.pow(a,i+1) + Math.pow(b,i+1) + Math.pow(c,i+1);
            System.out.println(answer);
        }
        
        return answer;
    }
}