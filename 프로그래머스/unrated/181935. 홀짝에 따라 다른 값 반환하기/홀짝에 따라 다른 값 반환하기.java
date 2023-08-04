class Solution {
    public int solution(int n) {
        int Odd_Sum = 0; int All_Sum = 0;
        for (int i = 1; i <= n; i++){
            if (i % 2 == 1){
                Odd_Sum += i;
            }
            else{
                All_Sum += Math.pow(i,2);    
            }
            
        }
        return (n % 2 == 1) ? Odd_Sum : All_Sum;
    }
}